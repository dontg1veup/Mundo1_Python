def fatorial (n,show=True):
    """
    Calcula o fatorial de um numero

    :param n: Numero a ser calculado o fatorial.
    :param show: Opcional se deseja ou nao mostrar a conta do fatorial.
    :return: O valor do fatorial do numero a ser calculado (n).

    """
    r = 1
    for c in range (n, 0, -1):
        if show:
            print (f"{c}", end=" ")
            if c != 1:
                print (f"x", end=" ")
            else:
                print ("=", end=" ")
        r = r * c
    return r

print (fatorial (6  ))

