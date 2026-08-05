lista = list()
c = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    c = c + 1

    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SsNn':
        print('Apenas S ou N')
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]

    if resp == 'N':
        break

print (f"Voce digitou {len(lista)} elementos")
lista.sort(reverse=True)
print (f"Os valores em ordem decrescente foram: {lista}")

if c in lista:
    print(f"O valor {c} faz parte da lista")
else:
    print(f"O valor {c} nao faz parte da lista")
