# Lendo o número do usuário
num = int(input("Digite um número entre 0 e 9999: "))

# Fazendo a mágica da matemática
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Mostrando o resultado na tela
print(f"Analisando o número {num}:")
print(f"Unidade: {u}")
print(f"Dezena:  {d}")
print(f"Centena: {c}")
print(f"Milhar:  {m}")