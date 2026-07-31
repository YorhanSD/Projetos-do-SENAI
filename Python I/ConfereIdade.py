entraLetra = input("Digite uma letra : ")

if entraLetra == "A" or entraLetra == "a" or entraLetra == "E" or entraLetra == "e" or entraLetra == "I" or entraLetra == "i" or entraLetra == "O" or entraLetra == "o" or entraLetra == "U" or entraLetra == "u":
    print("A letra digitada é uma vogal : ", entraLetra)
else:
    print("A letra digitada é uma consoante : ", entraLetra)

entraIdade = int(input("Digite sua idade : "))

if entraIdade >= 5 and entraIdade <= 7:
    print("Idade infantil A")
elif entraIdade >= 8 and entraIdade <= 11:
    print("Idade infantil B")
elif entraIdade >= 12 and entraIdade <= 13:
    print("Idade juvenil A")
elif entraIdade >= 14 and entraIdade <= 17:
    print("Idade juvenil B")
else:
    print("Adulto")