num = soma = count = 0
while num != 999:
    soma = soma + num
    num = int(input("Digite um numero:  "))
    if num != 999:
        count = count + 1
print(soma,count)