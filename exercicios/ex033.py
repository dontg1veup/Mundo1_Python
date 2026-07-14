menor = 0
maior = 0
for c in range(1,6):
    peso = int(input(f"Peso da {c} pessoa: "))
    if c == 1:
        menor = peso
        maior = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f"maior {maior} e menor {menor}")