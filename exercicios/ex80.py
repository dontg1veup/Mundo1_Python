from datetime import date

def voto (idade):
    if idade <=15:
        print (f"Voto opcional")
    elif idade >=18 and idade <=65:
        print (f"Voto Obrigatorio")
    else:
        print (f"Nao vota")

ano_atual = date.today().year

idade = ano_atual - int(input("Digite o ano de nascimento: "))

print ( f"Com {idade} anos: ",end="")
voto(idade)

