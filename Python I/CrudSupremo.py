para = False
#Usamos para estruturas que não sabemos quantas vezes ira ser repitida a instrução.

while (para == False): 
    print("Adção ---> 1")
    print("Subtração ---> 2")
    print("Multiplicação ---> 3")
    print("Divisão ---> 4")
    print("Descubra se o número é Par ou Ímpar ---> 5")
    print("Inicie e Determine a parada de uma Progressão Aritmetica ---> 6")
    print("Inicie e Determine a parada de uma Progressão Geometrica ---> 7")
    print("Fatorial ---> 8")
    print("Sequencia fibonacci ---> 9")
    print("Sair ---> 10")

    digiteUmaOpcao = int(input("Escolha entre uma das opções disponíveis : "))

    if(digiteUmaOpcao == 10):
        para = True
        print("Saindo... ")
        break
    
    if(digiteUmaOpcao == 1 or digiteUmaOpcao == 2 or digiteUmaOpcao == 3 or digiteUmaOpcao == 4 or digiteUmaOpcao == 5):

        numero1 = float(input("Digite um número : "))
        numero2 = float(input("Digite outro número : "))

    def selecione_operacao(digiteUmaOpcao):
            match digiteUmaOpcao:
                case 1:
                    calculo = numero1 + numero2
                    print("A soma dos dois números que você digitou é : ", calculo)
                case 2:
                    calculo = numero1 - numero2
                    print("A subtração dos dois números que você digitou é : ", calculo)
                case 3:
                    calculo = numero1 * numero2
                    print("A multiplicação dos dois números que você digitou é : ", calculo)      
                case 4:
                    calculo = numero1 / numero2
                    print("A divisão dos dois números que você digitou é : ", calculo)
                case 5:
                    if(numero1 % 2 == 0):
                        print("O número digitado é par : ",numero1)

                    if(numero2 % 2 == 0):
                        print("O número digitado é par : ",numero2)

                    if(numero1 % 2 != 0):
                        print("O número digitado é Ímpar : ",numero1)
                    
                    if(numero2 % 2 != 0):
                        print("O número digitado é Ímpar : ",numero2)
                case 6:
                    valorInicial = int(input("Digite um valor inicial : "))
                    valorExponencial = int(input("Digite um valor de soma : "))
                    valorTerminal = int(input("Digite um valor Terminal: "))

                    if(valorInicial < valorTerminal):
                        while(valorInicial < valorTerminal):
                            calculo = valorInicial = valorInicial + valorExponencial
                            print(calculo)
                    else:
                        while(valorInicial > valorTerminal):
                            calculo = valorInicial = valorInicial - valorExponencial
                            print(calculo)
                case 7:
                    valorInicial = int(input("Digite um valor inicial : "))
                    valorExponencial = int(input("Digite um valor de soma : "))
                    valorTerminal = int(input("Digite um valor Terminal: "))

                    if(valorInicial < valorTerminal):
                        while(valorInicial < valorTerminal):
                            calculo = valorInicial = valorInicial * valorExponencial
                            print(calculo)
                case 8:
                    digiteUmNumero = int(input("Digite um Número : "))
                    fatorial = 1
                    multiplicador = digiteUmNumero

                    while(multiplicador >= 1):
                        fatorial = fatorial * multiplicador
                        multiplicador = multiplicador -1
                        
                        print(fatorial, "!")

                case 9:
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

                case _:
                    return "Opção inválida!"    
        
    print(selecione_operacao(digiteUmaOpcao))    