lista = list ()
grupo = list ()
pesadas = list ()
leves = list ()
maispes = 0
maislev = 0
maispeslist = list ()
maislevlist = list ()
tot = 0
while True:

    lista.append(str(input("Digite o nome da pessoa: ")))
    lista.append(float(input("Digite o peso da pessoa: ")))
    if len(grupo) == 0:
        maispes = lista [1]
        maislev = lista [1]
    else:
        if lista [1] > maispes:
            maispes = lista[1]
        if lista [1] < maislev:
            maislev = lista[1]
    grupo.append(lista[:])

    lista.clear()

    answer = str(input("Deseja continuar? [S/N] "))
    if answer in "Nn":
        break

for pessoa in grupo:
    if pessoa[1] == maispes:
        maispeslist.append(pessoa[0])
    if pessoa[1] == maislev:
        maislevlist.append(pessoa[0])

print (grupo)
print (f"O maior peso foi de {maispes} Kg, peso de {maispeslist}  ")
print (f"O menor peso foi de {maislev} Kg peso de {maislevlist}")



