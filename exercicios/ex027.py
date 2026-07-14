soma = 0
for num in range (1,7):
    usernum = int(input("Digite um numero: "))
    if usernum % 2 == 0:
        soma = soma + usernum
print (soma)
