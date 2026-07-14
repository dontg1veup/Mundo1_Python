import datetime
menoridade = 0
maioridade = 0
for c in range(0,3):
    anonasc = int(input("Ano nascimento: "))
    idade = datetime.date.today().year - anonasc
    if idade < 18:
        menoridade = menoridade + 1
    else:
        maioridade = maioridade + 1
print(f"As pessoas de maior idade e menor idade sao respectivamente: {maioridade} e {menoridade}")