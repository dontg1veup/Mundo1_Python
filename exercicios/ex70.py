import datetime
dicionario = dict()
dicionario ["nome"] = str(input("Nome: "))
anonasc = int(input("Ano de nascimento: "))
dicionario ["idade"] = datetime.date.today().year - anonasc
dicionario ["carteira"] = int (input("Carteira de trabalho: "))
if dicionario ["carteira"] == 0:
    dicionario ["carteira"] = "Nao possui carteira"
else:
    dicionario ["contratacao"] = input("Seu ano de contratacao: ")
    dicionario ["salario"] = float(input("Seu salario: "))
    dicionario ["aposentadoria"] = dicionario ["idade"] + 30
for f, v in dicionario.items():
    print(f"{f} -> {v}")