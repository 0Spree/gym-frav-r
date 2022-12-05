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

    moduler2 = float(st.number_input(label="Hvor mange moduler har du for året?",step=1.,format="%.2f"))
    missingmoduler2 = float(st.number_input("Hvor mange moduler har du været fraværende? ",step=1.,format="%.2f"))

    udregning2 = round(procent2/moduler2 * missingmoduler2, 1)
    print(str(udregning2) + "%")
    st.text("Du har " + str(udregning2) + "% fravær")

code = '''BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBG5YYJYYYYYYYJJ?JJY5PGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBPYJ???JJJJJJJJ??7777777?YGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB5?777????JJJJJJ?77!!!!!!!!7?YGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBP7!!!777????JJJJ?777!!!~!777!!7JGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBY~~~~~!!!!7??JJYJ?77777!~!777!!!7JBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB5~~~^^^^~~~!??JYYJ?77777777?77!!~!75BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBG7~!!~~~!!!7??JJYYY?77?JY5555J7!7?YPPBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB5!!!77777???JJJYYYYJ7!77J5?!7?77?J5PYGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBJ!77??????JJJJYYYYYY?!!~!~~!!77?77??75BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBJ???JJJJJJJJYYYY555YJ?777777777?7777?PBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBYJJJYYYYJYYYYYY5555YYJ???????77777?JYBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB5YYYYYYYYY555555555YYJ????????????JYPBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGYY55555555555555555YJJ?????J5PP5YY5BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBP55555555PPPP5PP5555YJ?????J5Y?JJYPBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBG5555555PPPPPPPPP555YYJJ?JY5555YYPBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBG5YYY555PPPPGGPPP5555YJJ?7??7!?PBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB5YYYY55PPPPPGGGGPPP55YYJ?7!775BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBPYYYYYY55PPPPPGBBBBGGP55YJ?JYBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGYJJJJYY555555PPGGBBBBBGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBYJJJJYYY55555555PPGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGYJJJJJYY55YYY555PPGPGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGYJJJJJJJYYYYYY55PPYJGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB5J???????JJJJYY55Y?7?5BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGJ???77777777?JYYJ!!77JGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBP5YJJ???????7777!!!7?YGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGPPP555YYYYY55PGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'''
st.code(code, language='html')