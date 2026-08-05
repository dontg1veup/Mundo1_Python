from gettext import find

times_brasileirao = (
    "Vasco da Gama",
    "Internacional",
    "Bahia",
    "Botafogo",
    "Chapecoense",
    "Corinthians",
    "Coritiba",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Grêmio",
    "Internacional",
    "Mirassol",
    "Palmeiras",
    "Red Bull Bragantino",
    "Remo",
    "Santos",
    "São Paulo",
    "Athletico-PR",
    "Atletico-GO",
    "Vitória"
)

print(f"Os 5 primeiros times do Brasileirao sao: {times_brasileirao [:5]}")
print(f"Os 4 ultimos time do Brasileirao sao: {times_brasileirao[-4:]}")
print(f"Em ordem alfabetica: {sorted(times_brasileirao)} ")
posicao = times_brasileirao.index("Vasco da Gama")
print (f"O time do Vasco esta na {posicao + 1} posicao.")
