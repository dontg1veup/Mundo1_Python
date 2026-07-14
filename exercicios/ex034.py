media = 0
somaidade=0
maioridademasc = 0
nomevelho = ""
count = 0
for c in range(1, 6):
    nome = str(input(f"Digite o nome da {c} pessoa: ").upper().strip())
    idade = int(input(f"Digite a idade da {c} pessoa: ").strip())
    sexo = str(input(f"Digite o sexo da {c} pessoa: ").upper().strip())
    somaidade = somaidade + idade
    if sexo == "F" and idade <20:
        count = count + 1
    if sexo == "M" and idade>maioridademasc :
        maioridademasc = idade
        nomevelho = nome
media = somaidade / c
print(f"O nome do mais velho eh {nomevelho} e sua idade eh {maioridademasc}")
print(f"A quantidade de mulheres abaixo de 20 anos eh {count}")
print(f"A media de idade do grupo eh {media}")