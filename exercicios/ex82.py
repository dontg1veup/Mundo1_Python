def ficha (jogador="<desconhecido>",gols=0):
    print (f" O jogador {jogador} fez {gols} gols")

nome = str(input("Digite o nome do jogador: ")).strip()
numG = str (input("Digite o numero de gols: ")).strip()

if numG.isnumeric():
    numG = int(numG)
else:
    numG = 0

if nome.strip() == "":
    ficha (gols=numG)
else:
    ficha (nome,numG)
