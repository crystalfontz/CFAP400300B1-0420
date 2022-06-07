############################################################
# Raspberry Pi - CFAP400300B1 ePaper Interface Python Code #
############################################################

#########
# LICENSE
#
# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

#######################
# Software Requirements
#   - Python (code tested on a "Zero" on Raspberry Pi OS 11, Python 3.9.2)
#   - RPi.GPIO (availble in OS package manager or via pip)
#   - spidev (available from pip)
#   - Pillow (the Python Imaging Library) is an extremely useful tool for
#     building, loading, and exporting images to be rendered by the display.
#     It is available from pip, too.
#
######################################
# Hardware Connections / Configuration
#   - Raspberry Pi is configured with SPI interface active (see raspi-config)
#
#                         CFA-10084 Pin | RasPi Board Pin# | RasPi Pin Name
#   - Power Connections   --------------+------------------+---------------
#                             3.3v      |         1        |   3v3 Power
#                             GND       |         9        |   Ground
#   - SPI Connections     --------------+------------------+---------------
#                             SCK       |        23        |   SPI0 SCLK
#                             MOSI      |        19        |   SPI0 MOSI
#                             CS        |        26        |   SPI0 CE1
#   - Extra Connections   --------------+------------------+---------------
#                             D/C       |        22        |   GPIO 25
#                             RST       |        13        |   GPIO 27
#                             BUSY      |        18        |   GPIO 24
#
# NOTES:
#   - The breakout board (CFA-10084) requires the 0.47-ohm pads to be shorted
#     in order to be correctly interfaced with a CFAP400300B1. This can be
#     accomplished by placing a blob of solder over it. See:
#     https://www.crystalfontz.com/blog/why-does-my-epaper-display-not-work-with-my-epaper-adapter-board/
#   - The SPI pins are fully controlled by the spidev library, so there's no
#     need to explicitly control CE1 (CS) for indicating a SPI transmission
#     (as is done in the Arduino C code examples).
#   - A "command" versus a "data" transmission is indicated by setting the
#     D/C pin low or high, respectively prior to sending bytes over SPI.
#   - The "BUSY" pin is called the "READY" pin in the sample Arduino C code,
#     but it is actually labeled as "BUSY" on the breakout board. Operations
#     that run for a while set the BUSY pin high while they're in progress
#     and then to low when complete.
#   - Be advised while this code is in the public domain, the packages upon
#     which it depends are under their own respective licenses.


from PIL import Image, ImageDraw, ImageOps
import RPi.GPIO as GPIO
import spidev
from time import sleep


# Pin name constants:
EPD_DC = 22
EPD_RST = 13
EPD_BUSY = 18


class CFAP400300B1:
    def __init__(self):
        """Initialize CFAP400300B1 driver, resolution, etc. Runs once."""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(EPD_DC, GPIO.OUT)
        GPIO.setup(EPD_RST, GPIO.OUT)
        GPIO.setup(EPD_BUSY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.spi = spidev.SpiDev()
        self.spi.open(0, 1)
        self.spi.max_speed_hz = 2000000
        self.spi.mode = 0

        # Controller requires 3 initializations before it can be used
        for x in range(3):
            GPIO.output(EPD_RST, GPIO.LOW)
            sleep(0.020)
            GPIO.output(EPD_RST, GPIO.HIGH)
            sleep(0.020)

        # Initialize the Display
        self._write_command(0x01)
        self._write_data([0x03, 0x00, 0x2B, 0x2B])

        # Booster soft-start
        self._write_command(0x06)
        self._write_data([0x17, 0x17, 0x17])

        # Power on the display
        self._power_on()
        while GPIO.LOW == GPIO.input(EPD_BUSY):
            continue

        # Set OTPLUT
        self._write_command(0x00)
        self._write_data([0x93])

        # PLL Control
        self._write_command(0x30)
        self._write_data([0x3A])

        # Resolution
        self._write_command(0x61)
        self._write_data([0x01, 0x90, 0x01, 0x2C])

        # VCM DC Settings
        self._write_command(0x82)
        self._write_data([0x12])

        # VCOM and Data Interval
        self._write_command(0x50)
        self._write_data([0x07])

    def __del__(self):
        """Reset the GPIO to avoid GPIO warnings when program is restarted."""
        GPIO.cleanup(EPD_DC)
        GPIO.cleanup(EPD_RST)
        GPIO.cleanup(EPD_BUSY)

    def _write_command(self, command_hex):
        """Send a command byte to the display via SPI."""
        GPIO.output(EPD_DC, GPIO.LOW)
        self.spi.xfer2([command_hex])

    def _write_data(self, data_bytes):
        """Send data (following a previous (command) to the display via SPI."""
        GPIO.output(EPD_DC, GPIO.HIGH)
        self.spi.xfer2(data_bytes)

    def _power_on(self):
        """Turn on the display for receiving a new image / bytes."""
        self._write_command(0x04)

    def _power_off(self):
        """Display power off sequence. Display should be powered off after data
        is written to it.
        """
        self._write_command(0x02)
        self._write_command(0x03)
        self._write_data([0x00])

    def prepare_for_image(self):
        """Turns on the display, waits for it to be ready, then sends the
        necessary command to send image data."""
        self._power_on()
        while GPIO.LOW == GPIO.input(18):
            continue
        self._write_command(0x13)

    def refresh(self):
        """Following sending an image, trigger the display sequnce, wait for
        the refresh to complete, and turn off the display."""
        self._write_command(0x12)
        while GPIO.LOW == GPIO.input(18):
            continue
        self._power_off()

    def stripe_pattern(self):
        """Send a test pattern to the ePaper display."""
        for x in range(15000):
            self._write_data([0x0F])

    def all_black(self):
        """Fill the ePaper display with all black pixels."""
        for x in range(15000):
            self._write_data([0xFF])

    def all_white(self):
        """Fill the ePaper display with all white pixels."""
        for x in range(15000):
            self._write_data([0x00])

    def draw_bitmap(self, image_bytes):
        """Sends a whole bitmap to the display and refreshes (displays) it."""
        for byte in image_bytes:
            self._write_data([byte])


##############################################################
# Simple display initialization and placement of some drawings

# Initialize the display
screen = CFAP400300B1()

# Create a drawing canvas and put some shapes in it
original_img = Image.new("RGB", (400, 300), "white")
image_draw = ImageDraw.Draw(original_img)
image_draw.ellipse((10, 10, 50, 50), fill="white", outline="black", width=5)
image_draw.rectangle((60, 60, 100, 100), fill="white", outline="black", width=1)
image_draw.line((110, 100, 210, 10), fill="black", width=2)
image_draw.pieslice((220, 10, 310, 100), start=45, end=315, fill="black", outline="black", width=5)
image_draw.rounded_rectangle((320, 10, 390, 100), radius=15, fill="white", outline="black", width=8)

# Pillow inverts the image vs. what we expect when convert is called, undo it
bw_image = original_img.convert(mode="1", dither=Image.Dither.NONE)
inverted_img = ImageOps.invert(bw_image)

# Update the ePaper display with the created image
image_bytes = list(inverted_img.tobytes())
screen.prepare_for_image()
screen.draw_bitmap(image_bytes)
screen.refresh()

