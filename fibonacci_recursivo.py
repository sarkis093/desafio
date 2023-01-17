#!/usr/bin/python3
import sys

def fibonacci(n):
    if n in {0,1}:
         return n
    else:
        return (fibonacci(n -1) + fibonacci(n - 2))

num = int(input('Digite um limite de recursividade: '))

if num <= int(0):
    print('Número precisa ser maior que 0')
    sys.exit(1)

for x in range(num):
    print(fibonacci(x), end=' ')

print('\n')
