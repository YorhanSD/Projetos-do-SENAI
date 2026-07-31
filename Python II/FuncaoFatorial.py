def executafatorial(n):
    resultado = 1
    for n1 in range(n, 1, -1):
        resultado = resultado * n1
    return resultado

numero = int(input("Digite um número: "))
print("Fatorial:", executafatorial(numero))

