def contador (ini,fim,passo):
    if ini > fim:
        passo = -abs(passo)
        fim = fim -1
    else:
        fim = fim + 1
    for c in range(ini,fim,passo):
        print(f"{c} ",end=" ")



contador (1,-15,2)
print("")
contador (10,0,-2)
