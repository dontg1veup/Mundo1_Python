lista = list()
while True:
    valor = int(input("Digite um Valor inteiro: "))
    if valor not in lista:
        lista.append(valor)

    answer = str(input("Quer continuar? [S/N] ")).strip().upper()

    while True:
        if answer not in "SN":
            print("Digite apenas S ou N")
            answer = str(input("Quer continuar? [S/N] ")).strip().upper()
        else:
            break

    if answer == "N":
        break
    else:
        print('Vamos continuar...')

lista.sort()
print(lista)