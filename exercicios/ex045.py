import random
count = 0
while True:
    numbot = random.randint(1,100)

    while True:
        userchoice = input("Escolha PAR ou IMPAR: ").strip().upper()

        if userchoice not in ("PAR", "IMPAR"):
            print("Somente PAR ou IMPAR!")
        else:
            break
    numuser = int(input("Escolha um numero: "))

    if userchoice == "PAR":
        botchoice = "IMPAR"
    else:
        botchoice = "PAR"

    total = numbot + numuser

    if total % 2 == 0:
        result = "PAR"
    else:
        result = "IMPAR"

    print(f"Voce jogou {numuser} e o computador jogou {numbot}, total = {total} e deu... {result}")

    if userchoice == result:
        print("VOCE GANHOU!")
        count = count + 1
    else:
        print(f"VOCE PERDEU, O BOT ESCOLHEU {botchoice}")
        break

    print(f"Ja foram {count} vitorias consecutivas")

