import random
nomes = [
    input("Digite o primeiro nome"),
    input("Digite o segundo nome"),
    input("Digite o terceiro nome"),
    input("Digite o quarto nome")
]

escolhido = random.choice (nomes)
print(escolhido)