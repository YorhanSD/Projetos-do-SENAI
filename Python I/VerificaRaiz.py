import math

eRaiz = False

print ("Verificando se o número tem raiz inteira\n")

while (eRaiz == False):

    numero = int(input("Digite um número : \n"))

    raiz = math.sqrt(numero)
    raiz = round(raiz)

    if(raiz ** 2 == numero):
        
        print("A raiz desse número é : ", raiz)
        eRaiz = True
        break

    else:

        print("Esse número não tem raiz")   
        eRaiz = False 
        


            

        


    

    


#calculo = raiz / numero

#if(raiz == calculo): 
#     print("Raiz Valida : ", raiz)
# #else:
    # print("Raiz invalida")