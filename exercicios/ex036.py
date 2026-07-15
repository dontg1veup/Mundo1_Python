import random
count = 0
numbot = random.randint(1,10)

while True:
    numuser = int(input("Digite um numero: "))
    count += 1

    if numuser == numbot:
        if count == 1:
            print ("Acertou de primeira!")
        else:
            print("Acertou!")
        break
    elif numuser > numbot:
            print("Menos...")
    else:
            print("Mais...")
print (f"O numero de tentativas foi: {count}")