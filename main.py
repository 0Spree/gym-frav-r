import streamlit as st
# st.button('Click me')
if st.selectbox('Vil du regne i: ',['Moduler', 'Procent']) == 'Moduler':
    procent = 100
    moduler = st.number_input("Hvor mange moduler har du i perioden? ", 1, 600)
    missingmoduler = st.number_input("hvor mange moduler er du fraværende? ", 1, 600)

    udregning = round(procent/moduler * missingmoduler, 1)
    print(str(udregning) + "%")
    st.text("Du har " + str(udregning) + "% fravær")
else:
    procent = 100
    moduler = st.number_input("Hvor mange moduler har du i perioden? ", 1, 600)
    procentfravær = st.number_input("hvor mange procent fravær har du? ", 0, 100)
    udregning = round(moduler/procent * procentfravær, 2)
    print(str(udregning) + "%")
    st.text("Du har " + str(udregning) + " moduler med fravær")