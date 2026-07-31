seq = [0,1]

digiteLimite = int(input("Digite um número limite: "))

casaAnterior = -1
casaSucessora = 0

for n1 in range(0,digiteLimite,1):
    casaAnterior += 1
    casaSucessora += 1
    soma = (seq[casaAnterior] + seq[casaSucessora])
    seq.append(soma) #Adiciona soma ao array 
    print(soma)
