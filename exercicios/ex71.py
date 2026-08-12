dicionario = dict()
lista = list()
total = 0
dicionario ["nome"] = str(input("Nome: "))
quant = int(input("Quantidade de partidas: "))
for c in range(0, quant):
    gols = int(input("Quantidade de gols: "))
    total = total + gols
    lista.append(gols)
dicionario ["gols"] = lista [:]
dicionario ["total"] = total

print(dicionario)
print("-"*55)

for c , v in dicionario.items():
    print(f"O campo {c} tem o valor {v}")

print ("-"*55)

for i , v in enumerate(dicionario["gols"]):
    print(f" Na partida {i} fez {v} gols")
