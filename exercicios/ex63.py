mainlist = [[],[]]

for c in range (1, 8):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        mainlist[0].append(numero)
    else:
        mainlist[1].append(numero)

mainlist[0].sort()
mainlist[1].sort()

print (f"Os numeros pares foram: {mainlist[0]}")
print (f"Os numeros impares foram: {mainlist[1]}")