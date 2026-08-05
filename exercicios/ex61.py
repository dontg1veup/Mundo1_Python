expr = input("Digite a expressao ")
pilha = list()

for item in expr:
    if item == "(":
        pilha.append(item)
    elif item == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(item)
            break

if len(pilha) > 0:
    print('Expressao Invalida')
else:
    print('Expressao Valida')
