listadict = list ()
dicionario = dict ()
lista_gols = list ()
while True:
    dicionario ["nome"] = str(input("Qual nome do jogador:  "))
    quant = int (input(f"Quantas partidas {dicionario['nome']} jogou:  "))
    for c in range(0, quant):
        gols = int (input(f"Quantos gols na partida {c} "))
        lista_gols.append(gols)
    dicionario["gols"] = lista_gols [:]
    lista_gols.clear()
    listadict.append(dicionario.copy())
    while True:
        answer = input("Quer continuar? [S/N] ").strip().upper()[0]
        if answer in "NnSs":
            break
        else:
            continue
    if answer in "Nn":
        break

for index ,item in enumerate (listadict):
    print(f" {index} jogador: {item ["nome"]} gols: {item["gols"]} total: {sum(item["gols"])}")

while True:
    escolha = int(input("Mostrar dados de qual jogador: (999 para parar)"))
    if escolha == 999:
        break
    if escolha >= len(listadict):
        print (f"Nao existe jogador com esse codigo: {escolha}")
    else:
        print(f"Levantamento do jogador: {listadict[escolha]['nome']}")
        for i,gol in enumerate (listadict[escolha]["gols"],start=1):
            print(f"  partida {i} fez  {gol} gols")




