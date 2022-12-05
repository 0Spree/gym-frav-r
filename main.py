import streamlit as st
import time
# st.button('Click me')
st.header('Gymnasium fraværs beregner') 
if st.selectbox('Vil du regne for: ',['Perioden', 'Året']) == 'Perioden':
    procent = 100

    moduler = st.number_input("Hvor mange moduler har du i perioden? ", 1, 600)
    missingmoduler = st.number_input("Hvor mange moduler har du været fraværende? ", 1, 600)

    udregning = round(procent/moduler * missingmoduler, 1)
    print(str(udregning) + "%")
    st.text("Du har " + str(udregning) + "% fravær")

    #latest_iteration = st.empty()
    #bar = st.progress(0)
    #num = 10
#for i in range(num):
    #latest_iteration.text(f'{num - i}% ud af de tilladte 10%')
    #bar.progress((round(udregning)//num)*i)
    #time.sleep(1)
else:
    procent2 = 100.0

    moduler2 = float(st.number_input(label="Hvor mange moduler har du for året?",step=1.,format="%.2f", min_value=1.0, max_value=600.0))
    missingmoduler2 = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f", min_value=1.0, max_value=600.0))

    udregning2 = round(procent2/moduler2 * missingmoduler2, 5)
    print(str(udregning2) + "%")
    st.text("Du har " + str(udregning2) + "% fravær")

code = '''\.
 \\      .
  \\ _,.+;)_
  .\\;~%:88%%.
 (( a   `)9,8;%.
 /`   _) ' `9%%%?
(' .-' j    '8%%'
 `"+   |    .88%)+._____..,,_   ,+%$%.
       :.   d%9`             `-%*'"'~%$.
    ___(   (%C                 `.   68%%9
  ."        \7                  ;  C8%%)`
  : ."-.__,'.____________..,`   L.  \86' ,
  : L    : :            `  .'\.   '.  %$9%)
  ;  -.  : |             \  \  "-._ `. `~"
   `. !  : |              )  >     ". ?   
     `'  : |            .' .'       : |
         ; !          .' .'         : |
        ,' ;         ' .'           ; (
       .  (         j  (            `  \
'''
st.code(code, language='html')