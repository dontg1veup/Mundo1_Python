n1 = int (input("digite um numero inteiro "))
n2 = int (input("digite outro numero inteiro "))
n3 = int (input("digite outro numero inteiro "))

if n1 >= n2 and n1 >= n3:
    maior = n1
    print(f"O maior valor foi: {n1}")
elif n2 >= n1 and n2 >= n3:
    maior = n2
    print (f"O maior valor foi: {n2}")
else:
    maior = n3
    print(f"O maior valor foi: {n3}")

if n1 <= n2 and n1 <= n3:
    menor = n1
    print(f"O menor numero foi: {menor}")
elif n2 <= n1 and n2 <= n3:
    menor = n2
    print(f"O menor numero foi: {menor}")
else:
    menor = n3
    print(f"O menor numero foi: {menor}")