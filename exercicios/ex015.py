salario = int (input("Digite o seu salario: "))
if salario >= 1250:
    salario = salario + (salario * 10 / 100)
    print(salario)
else:
    salario = salario + (salario * 15 / 100)
    print(salario)
