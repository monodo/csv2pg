# matching dictionnary between provider field names and postgres database fieldnames
# SITN 2013

SwissMetNet = {
  '':'idobj',
  'time':'date_time',
  'stn':'station_id',
  'fve010z0':'vvit',
  'fkl010z1':'vraf',
  '':'vvscal',
  'Vvert':'vvert',
  '':'vvnorth',
  '':'vvest',
  'Vfreq':'vfreq',
  'dkl010z0':'vdir',
  '':'mbar',
  '':'ta',
  '':'t05',
  'tre200s0':'t2',
  'T10':'t10',
  'Tusa':'tusa',
  'Tpt100':'tpt100',
  '':'tnv',
  'Tdp':'tdp',
  '':'tpsy',
  '':'t36',
  'Tpt1000':'tpt1000',
  '':'hr',
  'ure200s0':'hr2',
  '':'ren',
  '':'rbil',
  '':'rglo',
  '':'rdur',
  'Patm':'patm',
  '':'patmr',
  '':'pvap',
  '':'prec_h',
  '':'prec_d',
  '':'prec_s',
  '':'neb',
  '':'alt850',
  '':'ti',
  '':'hi',
  'Te-1.471':'te_1471',
  'Te-0.513':'te_0513',
  '':'te_bat',
  '':'te_pan',
  '':'te_vt3_2',
  '':'te_vt3_10',
  'Tboit':'tboit',
  '':'tcell',
  '':'res1',
  '':'res2',
  '':'res3'
}

Combilog = {
  '':'idobj',
  'Date/Time':'date_time',
  '':'station_id',
  'Vvit':'vvit',
  'Vraf':'vraf',
  '':'vvscal',
  'Vvert':'vvert',
  '':'vvnorth',
  '':'vvest',
  'Vfreq':'vfreq',
  'Vdir':'vdir',
  '':'mbar',
  '':'ta',
  '':'t05',
  'T2':'t2',
  'T10':'t10',
  'Tusa':'tusa',
  'Tpt100':'tpt100',
  '':'tnv',
  'Tdp':'tdp',
  '':'tpsy',
  '':'t36',
  'Tpt1000':'tpt1000',
  '':'hr',
  'Hr2':'hr2',
  '':'ren',
  '':'rbil',
  '':'rglo',
  '':'rdur',
  'Patm':'patm',
  '':'patmr',
  '':'pvap',
  '':'prec_h',
  '':'prec_d',
  '':'prec_s',
  '':'neb',
  '':'alt850',
  '':'ti',
  '':'hi',
  'Te-1.471':'te_1471',
  'Te-0.513':'te_0513',
  '':'te_bat',
  '':'te_pan',
  '':'te_vt3_2',
  '':'te_vt3_10',
  'Tboit':'tboit',
  '':'tcell',
  '':'res1',
  '':'res2',
  '':'res3'
}

SamWi = {
    'date':'',
    'time':'',
    'R2':'',
    'NO':'no',
    'NO2':'no2',
    'NOX':'nox',
    'O3':'o3',
    'SO2':'so2',
    'PM10-C':'pm10_c',
    'PM10-M':'pm10_m',
    'Vvit':'vvit',
    'Vvit_2':'vvit_2',
    'mbar':'mbar',
    'Vdir':'vdir',
    'Ta':'ta',
    'Hr':'hr',
    'Ren':'ren',
    'PA':'patm',
    'Ti':'ti',
    'Hi':'hi',
    'PM10-Qop':'pm10_qop',
    'PM10-T1':'pm10_t1',
    'PM10-T2':'pm10_t2',
    'PM10-T3':'pm10_t3',
    'PM10-T4':'pm10_t4',
    'PM10-P1':'pm10_p1',
    'PM10-P2':'pm10_p2',
    'PM10-P3':'pm10_p3',
    'PM10-%off':'pm10_percent_off',
    'PM10-RM':'pm10_rm',
    'PM10-RH':'pm10_rh',
    'PM10-%HC':'pm10_percent_hc',
    'PM10-BCL':'pm10_bcl',
    'PM10-BCS':'pm10_bcs',
    'PM10-BC':'pm10_bc',
    'PM10-NA':'pm10_na',
    'PM10-NCF':'pm10_ncf',
    'PM10-NCL':'pm10_ncl',
    'PM10-NC':'pm10_nc',
    'PM2.5-C':'pm10_2_5c',
    'PM1':'pm1',
    'ppb':'ppb',
    'VOC-CH4':'voc_ch4',
    'VOC-n-CH4':'voc_n_ch4',
    'VOC-THC':'voc_thc',
    'BTX-Be':'btx_be',
    'BTX-To':'btx_to',
    'BTX-Ebe':'btx_ebe',
    'BTX-mX':'btx_mx',
    'BTX-pX':'btx_px',
}

Nabel = {
    'date':'',
    'time':'',
    'R2':'',
    'NO':'no',
    'NO2':'no2',
    'NOx':'nox',
    'O3':'o3',
    'SO2':'so2',
    'PM10_onl':'pm10_c',
    'PM10-M':'pm10_m',
    'WIGE':'vvit',
    'WIGEM':'vraf',
    'REGEN':'prec_h',
    'Vvit_2':'vvit_2',
    'mbar':'mbar',
    'WIRI':'vdir',
    'TEMP':'ta',
    'FEUCHTE':'hr',
    'STRGLO':'ren',
    'DRUCK':'patm',
    'Ti':'ti',
    'Hi':'hi',
    'PM10-Qop':'pm10_qop',
    'PM10-T1':'pm10_t1',
    'PM10-T2':'pm10_t2',
    'PM10-T3':'pm10_t3',
    'PM10-T4':'pm10_t4',
    'PM10-P1':'pm10_p1',
    'PM10-P2':'pm10_p2',
    'PM10-P3':'pm10_p3',
    'PM10-%off':'pm10_percent_off',
    'PM10-RM':'pm10_rm',
    'PM10-RH':'pm10_rh',
    'PM10-%HC':'pm10_percent_hc',
    'PM10-BCL':'pm10_bcl',
    'PM10-BCS':'pm10_bcs',
    'PM10-BC':'pm10_bc',
    'PM10-NA':'pm10_na',
    'PM10-NCF':'pm10_ncf',
    'PM10-NCL':'pm10_ncl',
    'PM10-NC':'pm10_nc',
    'PM2.5-C':'pm10_2_5c',
    'PM1':'pm1',
    'ppb':'ppb',
    'VOC-CH4':'voc_ch4',
    'VOC-n-CH4':'voc_n_ch4',
    'VOC-THC':'voc_thc',
    'BTX-Be':'btx_be',
    'BTX-To':'btx_to',
    'BTX-Ebe':'btx_ebe',
    'BTX-mX':'btx_mx',
    'BTX-pX':'btx_px',
}