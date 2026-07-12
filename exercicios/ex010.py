velocidade = int (input("Qual a velocidade do carro? "))
if velocidade > 80:
    print(f"voce foi multado, o total da multa fica em: {(velocidade-80)*7}")
else:
    print("voce nao foi multado")