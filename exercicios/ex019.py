import statistics


n1 = float (input("Qual a primeira nota?: "))
n2 = float (input("Qual a segunda nota?: "))
notas = (n1, n2)
media = statistics.median(notas)
if media >=7:
    print("Aprovado")
elif media >=5 and media <=6.9:
    print("recuperacao")
else:
    print("reprovado")
print(media)