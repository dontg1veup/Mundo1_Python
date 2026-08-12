import random
import time
dicionario = {}
lista = []
for c in range (1,5):
    dicionario['jogador'] = c
    dicionario ['dado'] = random.randint(1,6)
    print(f"O jogador {dicionario ['jogador']} tirou: {dicionario ['dado']} ")
    lista.append(dicionario.copy())
    time.sleep(1)
print("-"*35)
lista.sort(key=lambda item: item['dado'], reverse=True)
for index,item in enumerate (lista,start=1):
    print(f"O jogador {item['jogador']} tirou {item['dado']} e ficou em {index} lugar")


