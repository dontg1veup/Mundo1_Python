lista = list()

for c in range(0, 5):
    item = int(input("Digite um numero inteiro: "))
    if c==0 or item > lista[-1]:
        lista.append(item)
    else:
        for pos in range(0, len(lista)):
            if item <= lista[pos]:
                lista.insert(pos, item)
                break
print(lista)