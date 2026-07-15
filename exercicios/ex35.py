sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Digite o sexo [M/F]: ").upper().strip())
print(f"Seu sexo foi aceito!: {sexo}")