import random
import time
cont = 0
jogo = list ()
grupojogo = list ()
quant = int (input("Quantos jogos serao gerados ?: "))

for c in range (0, quant):
    while True:
        num = random.randint (1,60)
        if num not in jogo:
            cont += 1
            jogo.append(num)
        if cont >= 6:
            cont = 0
            grupojogo.append(jogo[:])
            jogo.clear()
            break


print ("Seus jogos foram:")

for jogo in grupojogo:
    jogo.sort()
    print (jogo)
    time.sleep(1)