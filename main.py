import streamlit as st
import pandas as pd
import numpy as np
# st.button('Click me')
st.header('Gymnasium fraværs beregner') 
# if st.selectbox('Vil du regne for: ',['Perioden', 'Året']) == 'Perioden':
choices = ['Perioden', 'Året']
#st.selectbox('Vil du regne for: ', (choices[0], choices[1]), label_visibility=st.session_state.visibility, disabled=st.session_state.disabled)
udregn_choice = st.radio("Udregn for ", key=choices[1], options=choices)

if udregn_choice == choices[0]:
    procent = 100
    maxp = int(10)
    moduler = float(st.number_input(label="Hvor mange moduler har du i perioden?",step=1.,format="%.2f", min_value=0., max_value=10000.))
    missingmoduler = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=0., max_value=10000.))
    

    if moduler < missingmoduler:
        st.text("Du kan ikke have flere fraværende moduler end moduler")
    else:
        try:
            udregning = round(procent/moduler * missingmoduler, 5)
        except ZeroDivisionError:
            udregning = 0
        
        st.text("Du har " + str(udregning) + r"% fravær")
        graf = maxp-udregning
        if float(graf) < -0.000001:
            st.text("Du har for meget")
        else:
            st.text("Du har " + str(graf) + r"% fravær tilbage ud af de 10% tilladte")
    


else:
    procent2 = 100.0
    maxp2 = 10
    moduler2 = float(st.number_input(label="Hvor mange moduler har du for året?",step=1.,format="%.2f", min_value=0., max_value=10000.))
    missingmoduler2 = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=0., max_value=10000.))
    #moduler2 = float(moduler2)
    #missingmoduler2 = float(missingmoduler2)
    # ekstra pjæk
    def pjek(moduler2, missingmoduler2):
        ekstraPjek = float(st.number_input("hvor mange moduler vil du gerne pjække for: "))
        if ekstraPjek != None:
            totalPjek = ((missingmoduler2 + ekstraPjek) / moduler2) * 100
            deltaPjek = (ekstraPjek / moduler2) * 100
            deltaPjek = round(deltaPjek, 3)
            totalPjek = round(totalPjek, 3)
            st.text("Dit instastede pjæk vil tælle for "+str(deltaPjek)+"%")
            st.text("Du vil have "+str(totalPjek)+"% hvis du pjekker i "+str(ekstraPjek)+" moduler")
    
    if moduler2 < missingmoduler2:
        st.text("Du kan ikke have flere fraværende moduler end moduler")
    else:
        try:
            udregning2 = round(procent2/moduler2 * missingmoduler2, 3)
        except ZeroDivisionError:
            udregning2 = 0
        
        st.text("Du har " + str(udregning2) + r"% fravær")
        graf = maxp2-udregning2
        if float(graf) < -0.000001:
            st.text("Du har for meget")
        else:
            st.text("Du har " + str(graf) + r"% fravær tilbage ud af de 10% tilladte")
    
    if moduler2 != 0:
        pjek(moduler2, missingmoduler2)




