import random
maior = float('-inf')
menor = float('inf')
tupla = ()

for i in range(10):
    numero = random.randint(1, 10)
    tupla = tupla + (numero,)
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(tupla)
print(max(tupla))
print(min(tupla))