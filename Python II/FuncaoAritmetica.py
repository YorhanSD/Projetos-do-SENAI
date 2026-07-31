def calculo(numero1, numero2, resposta):
    match resposta:
        case 1:
            return numero1 + numero2
        case 2:
            return numero1 - numero2
        case 3:
            return numero1 * numero2
        case 4:
            if numero2 == 0:
                return "Não é possível dividir por zero."
            return numero1 / numero2
        case _:
            return "Opção inválida"

while True:
    print("\nEscolha uma operação")
    print("Soma: 1")
    print("Subtração: 2")
    print("Multiplicação: 3")
    print("Divisão: 4")
    print("Sair: 5")

    resposta = int(input("Digite a opção: "))

    if resposta == 5:
        print("Saindo...")
        break

    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))

    resultado = calculo(numero1, numero2, resposta)
    print("O resultado da conta é:", resultado)
