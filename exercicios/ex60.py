lista = list()
pares = list()
impares = list()

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    answer = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while answer not in "SN":
        print('Resposta invalida')
        answer = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if answer == "N":
        break
 
print(lista)
print(pares)
print(impares)