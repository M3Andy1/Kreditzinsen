#Test file

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.write('This script helps to predict loan costs for fixed and variable interest rates Copright Andreas Puntigam')



st.write('Past Leitzins')
ezb_image = st.image('./chart.jpeg')
st.write('Predicted Leitzins every 2 years') 
EZB_Aufschlag=st.number_input('EZB Aufschalg',value=0.5)
Fix_Zins=st.number_input('Fix Zins',value=3.5)
col1, col2 = st.columns(2)
with col1:
    Start_zins=st.number_input('Start Leitzins 0',value=4.5)
    zins_2=st.number_input('2',value=3.5)
    zins_4=st.number_input('4',value=2)
    zins_6=st.number_input('6',value=2.5)
    zins_8=st.number_input('8',value=2.5)
    zins_10=st.number_input('10',value=2.0)
    zins_12=st.number_input('12',value=2.0)
    zins_14=st.number_input('14',value=3.0)
    st.write('Past Leitzins')
    ezb_image = st.image('./chart.jpeg')
    
with col2:

    zins_16=st.number_input('16',value=4.0)
    zins_18=st.number_input('18',value=4.0)
    zins_20=st.number_input('20',value=3.0)
    zins_22=st.number_input('22',value=2.0)
    zins_24=st.number_input('24',value=1.5)
    zins_26=st.number_input('26',value=1.5)
    zins_28=st.number_input('28',value=1.5)
    zins_30=st.number_input('30',value=1.5)
    st.write('Predicted Leitzins every year') 
    predicted_EZB=[Start_zins,zins_2,zins_4,zins_4,zins_6,zins_6,zins_8,zins_8,zins_10,zins_10,zins_12,zins_12,zins_14,zins_14,zins_16,zins_16,zins_18,zins_18,zins_20,zins_20,zins_22,zins_22,zins_24,zins_24,zins_26,zins_26,zins_28,zins_28,zins_30,zins_30]
    x_values = np.linspace(0, 29, 30)
    predicted_EZB_m_Aufschlag= [x + EZB_Aufschlag for x in predicted_EZB]
    Fixzins=np.linspace(Fix_Zins, Fix_Zins, 30)
    
    df = pd.DataFrame({'Years': x_values, 'Predicted EZB': predicted_EZB, 'predicted_EZB_m_Aufschlag': predicted_EZB_m_Aufschlag,'Fixzins': Fixzins})
    df.set_index('Years', inplace=True)
    st.line_chart(df)
    #st.line_chart(df, x="Years", y=["Predicted EZB","predicted_EZB_m_Aufschlag","Fixzins"])
    
    
st.write('Kredit Berechnung')
Kreditsumme=st.number_input('Kreditbetrag',value=300000)
Laufzeit=st.number_input('Laufzeit Jahre',value=30)
Fixzinsgarantie=st.number_input('Fixzinsgarantie in Jahren',value=15)


zero_zins_rate=Kreditsumme*1.05/Laufzeit

Kreditrestwert_fix=[]
Monatsrate_fix=[]
Restwert=Kreditsumme*1.05
for i in range (0,Laufzeit):
    
    if i<Fixzinsgarantie:
        Zinsen=Restwert*((Fix_Zins+EZB_Aufschlag)/100)
        Monatsrate_fix.append(Zinsen+zero_zins_rate)
        Restwert=Restwert-zero_zins_rate
        Kreditrestwert_fix.append(Restwert)
    else:
        Zinsen=Restwert*((predicted_EZB_m_Aufschlag[i]+EZB_Aufschlag)/100)
        Monatsrate_fix.append(Zinsen+zero_zins_rate)
        Restwert=Restwert-zero_zins_rate
        Kreditrestwert_fix.append(Restwert)


Kreditrestwert_variable=[]
Monatsrate_variable=[]
Restwert=Kreditsumme*1.05
for i in range (0,Laufzeit):
    
    Zinsen=Restwert*((predicted_EZB_m_Aufschlag[i]+EZB_Aufschlag)/100)
    Monatsrate_variable.append(Zinsen+zero_zins_rate)
    Restwert=Restwert-zero_zins_rate
    Kreditrestwert_variable.append(Restwert)


col1, col2 = st.columns(2)
with col1:
    st.write('Kreditrate pro Monat € mit Fixzins')
    st.write(np.mean(Monatsrate_fix)/12) 
    st.write('Gesamtrückzahlung fix zins')
    st.write(np.mean(Monatsrate_fix)*Laufzeit) 

with col2:
    st.write('Kreditrate pro Monat € mit Variablen Zins')
    st.write(np.mean(Monatsrate_variable)/12) 
    st.write('Gesamtrückzahlung variable')
    st.write(np.mean(Monatsrate_variable)*Laufzeit) 



#st.write(Monatsrate)
#st.write(Kreditrestwert) 



Gesamtrueckzahlung_fix=[]
cash=0
for a in range (0,Laufzeit):
    
    Gesamtrueckzahlung_fix.append(cash)
    cash=cash+Monatsrate_fix[a]
    
    
Gesamtrueckzahlung_variable=[]
cash=0
for a in range (0,Laufzeit):
    
    Gesamtrueckzahlung_variable.append(cash)
    cash=cash+Monatsrate_variable[a]
    
    
     
st.write(Gesamtrueckzahlung_fix)
st.write(Gesamtrueckzahlung_variable)     
    
    
    
    
Laufzeit_list=np.linspace(0, Laufzeit-1, Laufzeit)



df1 = pd.DataFrame({'Month': Laufzeit_list, 'Gesamtrueckzahlung Fix Zins': Gesamtrueckzahlung_fix, 'Gesamtrueckzahlung Variable Zins': Gesamtrueckzahlung_variable, 'Restwert Kredit': Kreditrestwert})
df1.set_index('Month', inplace=True)
st.line_chart(df1)