import random
alnum = random.randint (1,5)
usernum = int (input("Adivinhe o numeiro que o computador escolheu: ")) #jogador tenta adivinhar
if usernum==alnum:
    print(f"VOCE ACERTOU, PARABENS!!!")
else:
    print(f"voce errou...")
    print(f"o numero que o computador escolheu foi {alnum}")
