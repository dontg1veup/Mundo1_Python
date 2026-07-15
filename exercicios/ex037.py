menu=0
n1 = int(input("Digite um numero inteiro qualquer: "))
n2 = int(input("Digite outro numero inteiro qualquer: "))
while menu != 5:
    menu = int (input("O que deseja fazer?\n [1]somar\n [2]multiplicar\n [3]maior\n [4]novos numeros\n [5]Sair \n"))
    if menu == 1:
        soma = n1 + n2
        print(f"a soma desses valores eh: {soma}")
    elif menu == 2:
        multiplicacao = n1 * n2
        print(f"a multiplicacao desses valores eh: {multiplicacao}")
    elif menu == 3:
        if n1 == n2:
            print("os numeros sao iguais")
        elif n1 > n2:
            maior = n1
            print(f"o maior numero eh: {maior}")
        else:
            maior = n2
            print(f"o maior numero eh: {maior}")
    elif menu == 4:
        n1 = int(input("Digite um numero inteiro qualquer: "))
        n2 = int(input("Digite outro numero inteiro qualquer: "))
    elif menu == 5:
        print("Finalizando...")
    else:
        print ("Opcao invalida")


