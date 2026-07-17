s=n1=count=0
while True:
    n1 = int (input("Digite um numero inteiro [999 para parar]: "))
    if n1 == 999:
        break
    s = s + n1
    count = count + 1

print(f"A soma entre eles foi: {s} e a quantidade de itens foi: {count}")