total = count = contador = 0
pricecheapest = float ("inf")
while True:
    print("-="*20)
    print ("LOJA SUPER BARATAO")
    print ("-"*20)
    prod_name = input("Qual o nome do produto? ")
    price = float (input("Qual o preco ? R$: "))
    total = total + price
    if price > 1000:
        count = count + 1
    contador = contador + 1

    if price < pricecheapest:
        pricecheapest = price
        namecheapest = prod_name

    while True:
        resposta = input("Deseja continuar ? [S/N]: ").upper().strip()
        if resposta and resposta[0] in "NS":
            resposta = resposta [0]
            break
    if resposta == "N":
        break

print(f"O total foi : R${total}")
print(f"Preco acima de 1000 foi: {count}")
print(f"O produto mais barato foi: {namecheapest} e seu preco foi: {pricecheapest}")
