limite = int(input("Digite a quantidade de termos: "))
seq = [0, 1]

def gerar_fibonacci():
    
    if limite <= 0:
        print("Digite um número maior que zero.")
        return
        
    for _ in range(limite):
        
        proximo_numero = seq[-1] + seq[-2]
        seq.append(proximo_numero)
        print(proximo_numero)

gerar_fibonacci()
