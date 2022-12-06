import streamlit as st
import pandas as pd
import numpy as np
# st.button('Click me')
st.header('Gymnasium fraværs beregner') 
if st.selectbox('Vil du regne for: ',['Perioden', 'Året']) == 'Perioden':
    procent = 100
    maxp = int(10)
    moduler = float(st.number_input(label="Hvor mange moduler har du i perioden?",step=1.,format="%.2f", min_value=0., max_value=10000.))
    missingmoduler = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=0., max_value=10000.))

    try:
        udregning = round(procent/moduler * missingmoduler, 5)
    except ZeroDivisionError:
        udregning = 0
    
    st.text("Du har " + str(udregning) + "% fravær")
    graf = maxp-udregning
    if float(graf) <= 10.0:
        st.text("Du har " + str(graf) + "% fravær tilbage ud af de 10% tilladte")
    elif float(graf) < 0:
        st.text("Du har for meget")

    else:
        st.text("Idk")


else:
    procent2 = 100.0
    maxp2 = 10
    moduler2 = float(st.number_input(label="Hvor mange moduler har du for året?",step=1.,format="%.2f", min_value=0., max_value=10000.))
    missingmoduler2 = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=0., max_value=10000.))

    try:
        udregning2 = round(procent2/moduler2 * missingmoduler2, 5)
    except ZeroDivisionError:
        udregning2 = 0
    
    st.text("Du har " + str(udregning2) + "% fravær")
    graf = maxp2-udregning2
    if float(graf) <= 10.0:
        st.text("Du har " + str(graf) + "% fravær tilbage ud af de 10% tilladte")
    elif float(graf) < 0:
        st.text("Du har for meget")

    else:
        st.text("Idk")
