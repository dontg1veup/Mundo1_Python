frase = input("digite uma frase").strip().lower()
frase = frase.replace(" ", "")
palin = frase[::-1]
print(f"O inverso de {frase} eh: {palin}")
if frase == palin:
    print("Temos um palindromo")
else:
    print("Nao eh um palindromo")