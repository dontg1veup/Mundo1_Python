dicionario = {}

dicionario ['nome'] = input("Digite seu nome: ")
dicionario ['media'] = float (input("Digite sua media: "))

if dicionario['media'] >= 7:
    dicionario ['situacao'] = "aprovado"
else:
    dicionario ['situacao'] = "reprovado"

print(dicionario['nome'])
print(dicionario['media'])
print(dicionario['situacao'])