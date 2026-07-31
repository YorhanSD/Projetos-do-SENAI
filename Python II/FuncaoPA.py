numero = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

def pa(numero, razao):
    
    soma = 0

    for i in range(10):
        termo = numero + i * razao
        soma += termo
        print(f"{i+1} termo: {termo}")

    print("Soma dos termos:", soma)

pa(numero, razao)
