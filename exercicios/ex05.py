cidade = input("Digite o nome da cidade: ".strip().lower())
cidade = cidade.split()
print(cidade)
print (f'A cidade comeca com santo ?{"santo" in cidade[0]}')