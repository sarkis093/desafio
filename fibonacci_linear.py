#!/usr/bin/python3
import sys

num = int(input('Digite um limite de recursividade: '))

if num <= int(0):
    print('Número precisa ser maior que 0')
    sys.exit(1)

lista=[None] * num

for x in range(num):
    if not x > 1:
        lista[x]=x
    else:
        lista[x] = lista[x-1] + lista[x-2]

print(str(lista)[1:-1])
