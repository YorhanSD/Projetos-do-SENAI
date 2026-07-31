numero1 = int(input("Digite qualquer número : "))

def oraculoDosNumeros(numero1):
    if(numero1 % 2 == 0):
        print("O número digitado é par")
    else:
        print("O número digitado é ímpar")

print(oraculoDosNumeros(numero1))