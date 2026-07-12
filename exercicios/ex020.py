idade = int(input("Qual a sua idade? "))
if idade <= 9:
    categoria = "Mirim"
    print(f"{categoria}")
elif 9 < idade <= 14:
    categoria = "Infantil"
    print(f"{categoria}")
elif 14 < idade <= 19:
    categoria = "Junior"
    print(f"{categoria}")
elif idade == 20:
    categoria = "Senior"
    print(f"{categoria}")
else:
    categoria = "Master"
    print(f"{categoria}")
