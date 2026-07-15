primtermo = int (input("digite o primeiro numero"))
razao = int (input("digite a razao"))
termo = primtermo
count = 10
total = count
answer = 1
while count != 0:
    print (termo)
    termo = termo + razao
    count = count - 1
print (f"PAUSA")
while answer != 0:
    answer = int(input("Quantos termos deseja a mais ?"))
    contador = answer
    total = total + contador
    while contador != 0:
        print (termo)
        termo = termo + razao
        contador = contador - 1
print (f"Total de termos foi: {total}")