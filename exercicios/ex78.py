import random
from time import sleep

def sorteio (lista):

    print("SORTEANDO LISTA: ",end="")

    for c in range (0,5):
        numero = random.randint(0,10)
        lista.append(numero)
        print(f"{numero} ",end="")
        sleep(0.3)
    print("--FIM!--")
    sleep(1)
    return lista



def somaPares (lista):
    soma = 0
    print (f"SOMANDO PARES:",end="")
    for item in lista:
        if item % 2 == 0:
            soma = soma + item
    return soma

lista =[]
sorteio (lista)
print (somaPares (lista))



