estados = {
    "SP" : "São Paulo",
    "MG" : "Minas Gerais",
    "BA" : "Bahia"
}

paises = {
    "USA" : "United States",
    "ENG" : "England",
    "ESP" : "Spain"
}

estados = paises.copy()
print(estados)
print(paises)

paises.update(estados)

print(len(paises))