import calendar
import datetime as data
ano = int(input("Digite o ano que estamos:  "))
if ano == 0:
    ano = data.date.today().year
if calendar.isleap(ano):
    print(f"O ano de {ano} eh bissexto")
else:
    print("O ano nao eh bissexto")