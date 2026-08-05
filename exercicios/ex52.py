n1 = int (input("Digite um numero: "))
n2 = int (input("Digite outro numero: "))
n3 = int (input("Digite mais um numero: "))
n4 = int (input("Digite o ultimo numero: "))
tupla = (n1, n2, n3, n4)
count = 0
vezes = tupla.count(9)
primeironum = tupla.index(3)

for item in tupla:
    if item %2 == 0:
        count = count + 1
print(tupla)
print(vezes)
print(primeironum + 1)
print(f"Quantidade de itens pares: {count}")
