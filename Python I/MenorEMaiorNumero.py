primeiroNumero = float(input("Digite um número : "))
segundoNumero = float(input("Digite outro número : "))

if(primeiroNumero > segundoNumero):
    print(primeiroNumero, "é maior que ",segundoNumero)
else:
    print(segundoNumero, "é menor que ",primeiroNumero)

letra = input("Digite uma letra : ")

def verificar_letra(letra):
    match letra:
        case letra if letra == "C":
            return "Você é casado."
        case letra if letra == "S":
            return "Você é solteiro."
        case letra if letra == "D":
            return "Você é divorciado."
        case letra if letra == "V":
            return "Você é viúvo."
        case letra if letra == "O":
            return "Outros."
        case _:
            return "Letra Inválida."
        
print(verificar_letra(letra))
