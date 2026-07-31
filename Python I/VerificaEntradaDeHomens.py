numeroPessoas = int(input("Digite um número de pessoas : "))
quantidadeHomens = 0

for n1 in range(1, numeroPessoas, 1):

    digiteSexo = input("Digite o Sexo : ")

    if(digiteSexo == "m"):
        digiteSexo = "Masculino"
    elif(digiteSexo == "f"):
        digiteSexo = "Feminino"

    seq1 = [n1]
    seq2 = [digiteSexo]

    print("Pessoa : ",seq1," possui o sexo : ",seq2)

    if(digiteSexo == "Masculino"):
        quantidadeHomens += 1

print("Quantidade de Homens : ", quantidadeHomens)