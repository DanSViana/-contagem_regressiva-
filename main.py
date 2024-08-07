# importação de biblioteca
import os
import time

# entrada de dados 
numero = int(input('Informe um nomero inteiro: '))

while numero >= 0:
    print('\nContagem regressiva:')
    os.system('cls')
    print(f'{numero}...')
    numero -= 1
    time.sleep(1)
   
os.system('cls')
print('KABUUUMMMMM!!!!!!!')