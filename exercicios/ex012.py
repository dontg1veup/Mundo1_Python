distancia = int (input("Distancia em km"))
if distancia <= 200:
    valorpag = distancia * 0.50
else:
    valorpag = distancia * 0.45
print(valorpag)