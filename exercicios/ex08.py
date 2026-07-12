
nome = input ("Digite seu nome: ").strip()
name1 =  nome [:nome.find(" ")]
print(name1)
pos = nome.rfind (" ")
name2 = nome [pos+1:]
print(name2)
lista = nome.split()
firstname= lista[0]
lastname = lista [-1]
print(lastname)