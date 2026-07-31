letras = ["a","b","c"]

print("Tamanho da lista : ", len(letras))
print("Posição da letra A é : ", letras.index("a"))

nova = []
resp = ""

while resp != "sair":
    palavra = input("Digite uma palavra : ")
    print(palavra)
    nova.append(palavra)
    resp = input("Deseja sair: ").lower()
    if(resp == "sair"):
        break

print(nova)

