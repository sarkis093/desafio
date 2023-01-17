#!/usr/bin/python3
import sys

until = int(input('Digite um número: '))

if until <= int(1):
    print('Número precisa ser maior que 1...')
    sys.exit(1)

def eh_numero_primo(num,array_de_primos):
    for x in array_de_primos:
        if num % x == 0:
            return False
    return True

number=2
lista_numeros_primos=[]

while number <= until:
    if eh_numero_primo(number,lista_numeros_primos) == True:
        lista_numeros_primos.append(number)
    number += 1
print(lista_numeros_primos)