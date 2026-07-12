price = float (input("Digite o valor do produto: "))
payment = input("Como vai pagar ? 1=dinheiro / 2=cartao a vista / 3=2x no cartao / 4=3x no cartao ou mais")

if payment == "1":
    finalprice = price - (price*(10/100))
    print(f"{finalprice}")
elif payment == "2":
    finalprice = price - (price*(5/100))
    print(f"{finalprice}")
elif payment == "3":
    print(f"{price}")
else:
    finalprice = price + (price*(20/100))
    print(f"{finalprice}")
