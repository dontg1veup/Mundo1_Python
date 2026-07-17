agecount = countM_sexo = under20_female = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = ""
    while True:
        sexo = str(input("Digite o sexo: [F/M]")).upper().strip()[0]
        if sexo not in "FM":
            print("Digite apenas M ou F")
        else:
            break
    if idade > 18:
        agecount = agecount + 1
    if sexo == "M":
        countM_sexo = countM_sexo + 1
    if sexo == "F" and idade < 20:
        under20_female = under20_female + 1
    laco = input("Deseja continuar ? [S/N]").upper().strip()[0]

    while laco not in "SN":
        laco = input("Deseja continuar ? [S/N]").upper().strip()[0]
    if laco == "N":
        break

print(f"Acima de 18 anos: {agecount}")
print(f"Quantos homens foram cadastrados: {countM_sexo}")
print(f"Quantas mulheres menos de 20 anos: {under20_female}")
