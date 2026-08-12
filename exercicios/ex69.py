import random
import time
import operator
lista = list()
dicionario = {  "jogador1" : random.randint(1,6),
                "jogador2" : random.randint(1,6),
                "jogador3" : random.randint(1,6),
                "jogador4" : random.randint(1,6),
              }
for k,v in dicionario.items():
    print (f"O {k} tirou {v}")
    time.sleep(1)

lista = sorted(dicionario.items(), key=operator.itemgetter(1), reverse=True)
print(lista)
print("-"*30)
print("RANKING DOS JOGADORES")
for index,item in enumerate(lista,start=1):
    print (f"O {item[0]} tirou {item[1]} e ficou em {index} lugar")

