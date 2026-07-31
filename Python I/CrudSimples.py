sair = False

while (sair == False):

        print("1 = Adção")
        print("2 = Subtração")
        print("3 = Multiplicação")
        print("4 = Divisão")
        print("5 = Sair")

        numeroOpcao = float(input("Escolha uma Operação : "))
        
        if(numeroOpcao != 5):
                numero1 = float(input("Digite um número : \n"))
                numero2 = float(input("Digite outro número : \n"))

        def selecione_operacao(numeroOpcao):
                match numeroOpcao:
                        case numeroOpcao if numeroOpcao == 1:
                                calculo = numero1 + numero2
                                print("A soma dos dois números que você digitou é : ", calculo)
                                return "Você selecinou soma\n"
                        case numeroOpcao if numeroOpcao == 2:
                                calculo = numero1 - numero2
                                print("A subtração dos dois números que você digitou é : ", calculo)
                                return "Você selecinou subtração\n"
                        case numeroOpcao if numeroOpcao == 3:
                                calculo = numero1 * numero2
                                print("A multiplicação dos dois números que você digitou é : ", calculo)
                                return "Você selecinou multiplicação\n"
                        case numeroOpcao if numeroOpcao == 4:
                                calculo = numero1 / numero2
                                print("A divisão dos dois números que você digitou é : ", calculo)
                                return "Você selecinou divisão\n"
                        case numeroOpcao if numeroOpcao == 5:
                                return "Saindo..."
                        case _:
                                return "Opção inválida!"

        if(numeroOpcao == 5):
                sair = True 

        print(selecione_operacao(numeroOpcao))    