
seq = []

for n1 in range(0,5,1):
        
        digiteNumero = int(input("Digite um número: "))

        seq.append(digiteNumero)

        print("Você digitou:", digiteNumero)

        print("Entrada inválida! Digite apenas números inteiros.")

        exit(1)

soma = sum(seq)
media = soma / len(seq)

print("\nNúmeros digitados:", seq)
print("Soma:", soma)
print("Média:", media)
