fatorial = int(input("Digite outro número : "))
multiplicador = fatorial - 1

for n1 in range(fatorial,1,-1):
    fatorial = fatorial * multiplicador
    multiplicador -= 1
    print(fatorial)