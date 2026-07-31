seq = []

digiteInicio = int(input("Digite o valor inicial (tem que ser diferente de 0): "))
digiteUmLimite = int(input("Digite um limite: "))
digiteUmaMultiplicacao = int(input("Digite a razão da PG: "))

valor = digiteInicio

for n1 in range(1,digiteUmLimite,1):
    seq.append(valor)
    valor *= digiteUmaMultiplicacao

print(seq)
