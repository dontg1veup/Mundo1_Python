answer = "S"
soma = 0
count = 0
maior = 0
menor = 0
while answer == "S":
    num = int(input("Digite um Numero: "))
    soma = soma + num
    count = count + 1
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    answer = input("Quer continuar ? [S/N]: ").upper().strip()[0]
media = soma / count
print(soma)
print(count)
print(media)
print(maior)
print(menor)
