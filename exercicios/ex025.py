soma = 0
for number in range(0, 501):
    if number % 2 == 1 and number % 3 == 0 :
        soma = soma + number

print(f"A soma eh {soma}, e o numero desse laco eh: {number}")