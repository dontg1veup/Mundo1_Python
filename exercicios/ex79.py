def escopo (b):
    global a

    a = a + 3
    print (f"A dentro vale {a}")


a = 5
escopo (a)
print (f"A fora vale {a}")
