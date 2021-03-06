#ifndef __LUTS_FOR_CFAP400300B00420_H__
#define __LUTS_FOR_CFAP400300B00420_H__
//=============================================================================
// "Arduino" example program for Crystalfontz ePaper. 
//
// This project is for the CFAP400300B0-0420 :
//
//   https://www.crystalfontz.com/product/cfap400300b00420
//=============================================================================
// Formatted to work with WriteCMD_StringFlash(), first byte is command,
// remainder are data
const uint8_t VCOM_LUT_LUTC[]      PROGMEM =
{ 
  0x00	,0x08	,0x00	,0x00	,0x00	,0x02,
  0x60	,0x28	,0x28	,0x00	,0x00	,0x01,
  0x00	,0x14	,0x00	,0x00	,0x00	,0x01,
  0x00	,0x12	,0x12	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00, };
const uint8_t W2W_LUT_LUTWW[]      PROGMEM =
{
  0x40	,0x08	,0x00	,0x00	,0x00	,0x02,
  0x90	,0x28	,0x28	,0x00	,0x00	,0x01,
  0x40	,0x14	,0x00	,0x00	,0x00	,0x01,
  0xA0	,0x12	,0x12	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
const uint8_t B2W_LUT_LUTBW_LUTR[] PROGMEM =
{
  0x40	,0x17	,0x00	,0x00	,0x00	,0x02	,
  0x90	,0x0F	,0x0F	,0x00	,0x00	,0x03	,
  0x40	,0x0A	,0x01	,0x00	,0x00	,0x01	,
  0xA0	,0x0E	,0x0E	,0x00	,0x00	,0x02	,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00	,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00	,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00	,
};
const uint8_t B2B_LUT_LUTBB_LUTB[] PROGMEM =
{
  0x80	,0x08	,0x00	,0x00	,0x00	,0x02,
  0x90	,0x28	,0x28	,0x00	,0x00	,0x01,
  0x80	,0x14	,0x00	,0x00	,0x00	,0x01,
  0x50	,0x12	,0x12	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
const uint8_t W2B_LUT_LUTWB_LUTW[] PROGMEM =
{
  0x80	,0x08	,0x00	,0x00	,0x00	,0x02,
  0x90	,0x28	,0x28	,0x00	,0x00	,0x01,
  0x80	,0x14	,0x00	,0x00	,0x00	,0x01,
  0x50	,0x12	,0x12	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
//=============================================================================

const uint8_t VCOM_LUT_LUTC_PARTIAL[]      PROGMEM =
{
  0x00, 0x19, 0x01, 0x00, 0x00, 0x01,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, };
const uint8_t W2W_LUT_LUTWW_PARTIAL[]      PROGMEM =
{
  0x00	,0x19	,0x01	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
const uint8_t B2W_LUT_LUTBW_LUTR_PARTIAL[] PROGMEM =
{
  0x80	,0x19	,0x01	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
const uint8_t B2B_LUT_LUTBB_LUTB_PARTIAL[] PROGMEM =
{
  0x00	,0x19	,0x01	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
const uint8_t W2B_LUT_LUTWB_LUTW_PARTIAL[] PROGMEM =
{
  0x40	,0x19	,0x01	,0x00	,0x00	,0x01,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
  0x00	,0x00	,0x00	,0x00	,0x00	,0x00,
};
//=============================================================================
#endif 
