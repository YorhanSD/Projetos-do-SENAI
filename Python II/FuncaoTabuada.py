numero = int(input("Digite um número : "))

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabuada(numero)