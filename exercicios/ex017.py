n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))

if n1 > n2:
    print(f"{n1} e maior que {n2}")
elif n2 > n1:
    print(f"{n2} e maior que {n1}")
else:
    print(f"{n1} e igual a {n2}")