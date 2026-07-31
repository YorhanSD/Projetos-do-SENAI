numero = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

def pg(numero, razao):
    multiplicacao = 1

    for i in range(10):
        termo = numero * (razao ** i)
        multiplicacao *= termo
        print(f"{i+1}º termo: {termo}")

    print("Multiplicação dos termos:", multiplicacao)

pg(numero, razao)