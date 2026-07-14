numero = int(input("digite um numero"))
count = 0
for num in range(1,numero+1):
    if  numero % num == 0:
        count = count + 1
        print (f"Seu numero eh divisivel por {num}")

if count > 2:
    print("seu numero nao eh primo")
else:
    print("seu numero eh primo")
