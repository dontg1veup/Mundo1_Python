def maior (*numeros):
    maior = 0
    count = 0
    for numero in numeros:
        if count == 0:
            maior = numero
        if numero > maior:
            maior = numero
        count += 1
    print (f"Maior eh igual a {maior}")
    

maior (9,5,8)



