from random import*

#PROGRAMA DE DADO USANDO LIBRERIA RANDOM

print('!JUEGO DE TIRA EL DADO¡')

dado = randint(1,6)
if dado == 6:
    print(f'Ganaste')
    print(f'Te Salio {dado}')
else: 
    print(f'Te Salio {dado}')
    print(f'Sigue Intentando')