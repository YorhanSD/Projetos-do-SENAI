listaNumI = []
listaNumII = []
listaSoma = []

for i in range(10):
    numero = float(input("Digite um número : "))
    print("Você digitou : ", numero)
    listaNumI.append(numero)

print(listaNumI)
print()

for i in range(10):
    numero = float(input("Digite um número : "))
    print("Você digitou : ", numero)
    listaNumII.append(numero)

print(listaNumII)
print()

print("A soma das duas listas é :")

for i in range(10):
    resultado = listaNumI[i] + listaNumII[i]
    listaSoma.append(resultado)
    print(listaNumI[i]," + ",listaNumII[i]," = ",resultado)

print()
print(listaNumI)
print(listaNumII)
print(listaSoma)
    

