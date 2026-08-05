tupla = ('zero','um', 'dois', 'tres', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

desejo = int (input("Escolha um numero entre 0 e 20: "))

while desejo <0 or desejo > 20:
    desejo = int(input("Escolha um numero entre 0 e 20: "))

print(f"Voce digitou o numero {tupla[desejo]}")