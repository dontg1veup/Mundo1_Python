def titulo(txt):
    tam = len(txt) + 4
    print ('-'*tam)
    print (f"{txt.center(tam)}")
    print ('-'*tam)

titulo('Curso em video Python')
titulo('CeV')