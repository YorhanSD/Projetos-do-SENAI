#Exercicio Extra

numero1 = float(input("Digite um número : "))
numero2 = float(input("Digite outro número : "))
numero3 = float(input("Digite mais um número : "))

z = 0 # Maior valor
y = 0 # Valor Intermediario
x = 0 # Menor valor

if(numero1 >= numero2 and numero1 >= numero3 and numero3 >= numero2):
    z = numero1
    y = numero3
    x = numero2
elif(numero2 >= numero1 and numero2 >= numero3 and numero1 >= numero3):
    z = numero2
    y = numero1
    x = numero3
elif(numero3 >= numero1 and numero3 >= numero2 and numero2 >= numero1):
    z = numero3
    y = numero2
    x = numero1

print("Menor valor : \n", x)
print("Valor intermediario : \n", y)
print("Maior valor : \n", z)