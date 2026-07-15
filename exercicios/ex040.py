primtermo = 0
seguntermo = 1
somaterm = seguntermo + primtermo
contador = 0
while contador < 10:
    print(f"{primtermo}")
    primtermo = seguntermo
    seguntermo = somaterm
    somaterm = seguntermo + primtermo
    contador = contador +  1