soma = media = 0
dicionario = dict ()
galera = list ()

while True:
    dicionario.clear()
    dicionario ["nome"] = input("Qual o seu nome? ")
    while True:
        dicionario ["sexo"] = input("Qual o seu sexo? ")
        if dicionario ["sexo"] in "fF":
            mulheres = dicionario["nome"]
        if dicionario ["sexo"] not in "MmFf":
            print("Comando Invalido, apenas M ou F")
            continue
        else:
            break
    dicionario ["idade"] = int (input("Qual a sua idade? "))
    soma = soma + dicionario["idade"]
    while True:
        answer = input("Deseja continuar? [S/N] ")
        if answer not in "SsNn":
            print("Comando Invalido, apenas S ou N")
            continue
        else:
            break
    galera.append(dicionario.copy())


    if answer in "Nn":
        break

media = soma / len(galera)
print (f"O total de pessoas foi: {len(galera)}")
print (f"A media de idade eh: {media:5.2f}")
print (f"As mulheres cadastradas foram: ")
for p in galera:
    if p["sexo"] in "Ff":
        print (p["nome"])

for p in galera:
    if p["idade"] > media:
        print (f" As pessoas acima da idade media foram: {p['nome']}")





