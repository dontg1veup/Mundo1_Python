from datetime import date
actualyear = date.today().year
yearborn = int(input("Digite o ano de nascimento do atleta: "))
age = actualyear - yearborn

if age < 18:
    time = 18 - age
    print(f"Falta {time} anos para o alistamento ")
elif age == 18:
    print("Voce deve se alistar")
else:
    time = age - 18
    print(f"Passou {time} desde que voce deveria ter se alistado")