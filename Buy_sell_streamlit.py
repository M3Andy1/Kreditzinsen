# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:42:16 2024

@author: andy2
"""

import pandas as pd
from pandas import Series, DataFrame
import pandas_ta as ta
from ta import add_all_ta_features
from ta.utils import dropna
import numpy as np
import matplotlib.pyplot as plt

import pandas_datareader.data as web
from datetime import datetime
import logging
from datetime import timedelta
#from Functions_ML import check_Start
from datetime import date
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_analysts_info
import math
from functions_trend_algo import get_ohlc_weeks,get_high_lows,del_double_values,calc_avg_volume,add_first_and_last_entry,replace_nan,trend_identification,get_high_lows_combined

from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates

tech_list=[]
kurs_ziele_list=[]

dates_analysen=[]
datafile = open('List_AP_kurs_ziel.txt','r')
#datafile = open('Aktienliste_actual_stocks.txt','r')
for line in datafile:
    temp=line.split(";")
    tech_list.append(temp[0])
    temp_kz=[]
    temp_kz_corr=[]
    temp_kursziele=temp[1].split(",")

    for i in range(0,len(temp_kursziele)):
        temp_kz.append(float(temp_kursziele[i]))
    dates_analysen.append(temp[2])

    kurs_ziele_list.append(temp_kz)

    



List_Aktien_rating=pd.DataFrame(columns=['Stock','Performance_last_week [%]','1 Year performance [%]','2 Year performance [%]','Trend_mittelfristig','Trend_langfristig','Volumen_langfristig_increase [%]','Bestätigung OBV','MACD-Status','RSI & MOM- Status','Change Status Trend - mittel', 'Change Status Trend - lang','Change Status OBV','Change Status Bottom increase','Change Status Top increase','Bottom_Increase_status','Trend läuft seit:','Performance_trend_mittelfristig','V2-Status','V1-Status','Aktuelle Kursziel','Höchste erreichte Kursziel','Max_Kz','Change_KZ_erreicht','PC_to_next_KZ'])
List_Aktien_change=pd.DataFrame(columns=['Stock','Trend_mittelfristig','Trend_langfristig','Bestätigung OBV','MACD-Status','RSI & MOM- Status','Change Status Trend - mittel', 'Change Status Trend - lang','Change Status OBV','V2-Status','V1-Status','Aktuelle Kursziel','Höchste erreichte Kursziel','Max_Kz','Change_KZ_erreicht','Change_V1_Status','PC_to_next_KZ'])
