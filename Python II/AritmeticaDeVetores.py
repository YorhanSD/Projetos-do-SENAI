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

print("Soma ---> 1")
print("Subtração ---> 2")
print("Multiplicação --- > 3")
print("Divisão ---> 4")

resp = int(input("Escolha uma das operações : "))

if(resp == 1):
    for i in range(10):
        resultado = listaNumI[i] + listaNumII[i]
        listaSoma.append(resultado)
        print(listaNumI[i]," + ",listaNumII[i]," = ",resultado)

    print()
    print(listaNumI)
    print(listaNumII)
    print(listaSoma)

if(resp == 2):
    for i in range(10):
        resultado = listaNumI[i] - listaNumII[i]
        listaSoma.append(resultado)
        print(listaNumI[i]," - ",listaNumII[i]," = ",resultado)

    print()
    print(listaNumI)
    print(listaNumII)
    print(listaSoma)

if(resp == 3):
    for i in range(10):
        resultado = listaNumI[i] * listaNumII[i]
        listaSoma.append(resultado)
        print(listaNumI[i]," X ",listaNumII[i]," = ",resultado)

    print()
    print(listaNumI)
    print(listaNumII)
    print(listaSoma)

if(resp == 4):
    for i in range(10):
        resultado = listaNumI[i] / listaNumII[i]
        listaSoma.append(resultado)
        print(listaNumI[i]," / ",listaNumII[i]," = ",resultado)

    print()
    print(listaNumI)
    print(listaNumII)
    print(listaSoma)
    

