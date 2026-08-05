import math

lista = list()
maior = -math.inf
menor = math.inf
indexmai = list()
indexmen = list()
for c in range(0, 5):
    lista.append(int(input("Digite um numero inteiro: ")) )
print(lista)

for index, item in enumerate(lista):
    print(f"O indice foi {index} e o valor foi {item}")
    if item > maior:
        maior = item
    if item < menor:
        menor = item

for index,item in enumerate(lista):
    if item == maior:
        indexmai.append(index)
    if item == menor:
        indexmen.append(index)


print(f"O maior item foi {maior} nas posicoes {indexmai} e o menor foi {menor} na posicao {indexmen}")