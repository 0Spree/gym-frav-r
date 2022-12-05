import streamlit as st
import pandas as pd
import numpy as np
# st.button('Click me')
st.header('Gymnasium fraværs beregner') 
if st.selectbox('Vil du regne for: ',['Perioden', 'Året']) == 'Perioden':
    procent = 100
    maxp = int(10)
    moduler = float(st.number_input(label="Hvor mange moduler har du i perioden?",step=1.,format="%.2f", min_value=0.001, max_value=600.0))
    missingmoduler = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=0.001, max_value=600.0))

    udregning = round(procent/moduler * missingmoduler, 1)
    print(str(udregning) + "%")
    st.text("Du har " + str(udregning) + "% fravær")

    graf = round(maxp-udregning)
    if [maxp] < [graf]:
        st.text("Du har " + str(graf) + "% fravær tilbage ud af de 10% tilladte")
    else:
        st.text("Du har for meget")

else:
    procent2 = 100.0
    maxp2 = 10
    moduler2 = float(st.number_input(label="Hvor mange moduler har du for året?",step=1.,format="%.2f", min_value=0.001, max_value=600.0))
    missingmoduler2 = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=0.001, max_value=600.0))

    udregning2 = round(procent2/moduler2 * missingmoduler2, 5)
    st.text("Du har " + str(udregning2) + "% fravær")
    
    graf2 = round(maxp2-udregning2, 2)
    if maxp2 > graf2:
        st.text("Du har " + str(graf2) + "% fravær tilbage ud af de 10% tilladte")
    else: print("Du har for meget")
