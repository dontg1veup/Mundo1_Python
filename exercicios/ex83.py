def leiaInt(msg):

    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f"ERRO!")


n = leiaInt('Digite um numero: ')

print (n)