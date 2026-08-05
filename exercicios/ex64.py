matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap = 0
somathirdcol = 0
maiorval = 0
for c in range(0,3):
    for c1 in range(0,3):
        matriz [c] [c1] = int(input(f"Digite um valor para {c,c1}"))
        if matriz[c][c1] % 2 == 0:
            somap = somap + matriz[c][c1]
        if c1 == 2:
            somathirdcol = somathirdcol + matriz[c][c1]
        if c1 == 1:
            if c == 0:
                maiorval = matriz[c][c1]
            else:
                if matriz[c][c1] > maiorval:
                    maiorval = matriz[c][c1]



for c in range(0,3):
    for c1 in range(0,3):
        print(f" {matriz[c] [c1]} ",end="")
    print ()
print (f"A soma dos pares foi: {somap}")
print (f"A soma dos valores da terceira coluna foi : {somathirdcol}")
print (f"O maior valor da 2 coluna foi : {maiorval}")





