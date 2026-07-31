#OPERADORES LÓGICOS

#IDENTAÇÃO
# Usamos para fazer as marcações para os códigos que vão dentro dos marcadores lógicos

# Marcadores Lógicos: IF, WHILE E FOR

# == IGUAL
# != DIFERENTE
# > MAIOR QUE
# < MENOR QUE
# >= MAIOR OU IGUAL QUE
# <= MENOR OU IGUAL QUE

# Exemplo : Média Anual:

nota1 = float(input("Digite sua nota do primeiro trimestre : \n"))
nota2 = float(input("Digite sua nota do segundo trimestre : \n"))
nota3 = float(input("Digite sua nota do terceiro trimestre: \n"))
nota4 = float(input("Digite sua nota do quarto trimestre : \n"))

mediaAnual = (nota1 + nota2 + nota3 + nota4) / 4

print("Sua média foi de : ", mediaAnual, "\n")

if(mediaAnual >= 6): #If é sempre acompanhado de uma condicional
    print("Aprovado")
else: #Nunca acompanha uma condição
    print("Reprovado")

