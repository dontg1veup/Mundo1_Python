import random
import time
user = int (input("Faca sua escolha: 1=Pedra, 2=Papel, 3=Tesoura "))
bot = random.randint(1,3)
while user not in [1,2,3]:
    user = int (input("Comando invalido, refaca sua escolha:\n 1=Pedra, 2=Papel, 3=Tesoura \n \n"))
if user == 1:
    categoriauser = "Pedra"
elif user == 2:
    categoriauser = "Papel"
else:
    categoriauser = "Tesoura"



if bot == 1:
    categoriabot = "Pedra"
elif bot == 2:
    categoriabot = "Papel"
else:
    categoriabot = "Tesoura"
print(f" O bot vai escolher")
time.sleep(3)

print(f"O bot escolheu: {categoriabot}!")
print (f"Voce escolheu: {categoriauser}!")

if categoriauser == "Pedra":
    if categoriabot == "Papel":
        print("Voce Perdeu!")
    elif categoriabot == "Tesoura":
        print("Voce Ganhou!")
    else:
        print("Empate!")
elif categoriauser == "Papel":
    if categoriabot == "Pedra":
        print("Voce Ganhou!")
    elif categoriabot == "Tesoura":
        print("Voce Perdeu!")
    else:
        print("Empate!")
elif categoriauser == "Tesoura":
    if categoriabot == "Pedra":
        print("Voce Perdeu!")
    elif categoriabot == "Papel":
        print("Voce Ganhou!")
    else:
        print("Empate!")
