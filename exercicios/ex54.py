palavras = ("palavras", "aprender", "programar", "linguagem", "python","curso", "grupo","praticar","trabalhar","mercado","programador","futuro")


for item in palavras:
    print(f"\nNa palavra {item.upper():.<10} temos as vogais: ", end="")
    for letra in item:
        if letra in "aeiou":
            print(letra, end="")



