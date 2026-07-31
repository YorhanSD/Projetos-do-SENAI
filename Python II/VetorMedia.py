notas = []

for i in range(4):
    numero = float(input("Digite uma nota : "))
    notas.append(numero)

print()
print(notas)

total = 0
for i in range(0,len(notas),1):
    total += notas[i]
    print("Nota : ", notas[i])

resultado = total / len(notas)

print()
print("Média : ", resultado)