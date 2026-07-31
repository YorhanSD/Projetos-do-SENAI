idade = int(input("Digite sua idade : "))

def verificar_idade(idade):
    match idade:
        case idade if idade < 18:
            return "Entrada Permitida: Você é menor de idade."
        case idade if idade >= 18:
            return "Entrada Proibida : Você é maior de idade."
        case _:
            return "Idade inválida."
        
print(verificar_idade(idade))
