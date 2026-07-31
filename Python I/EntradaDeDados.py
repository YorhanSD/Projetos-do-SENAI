usuarioDigitaNome = input("nome : ")

print("seu nome é : ", usuarioDigitaNome)

if(usuarioDigitaNome == "nome"): input("seu nome certamente não é nome")

primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite outro número : "))

calculo = primeiroNumero + segundoNumero;

print ("somando os números se obtem : ", calculo)

calculo = primeiroNumero * segundoNumero;

print("multiplicando os números se obtem : ", calculo)

calculo = primeiroNumero - segundoNumero;

print("subtraindo os números se obtem : ", calculo)

calculo = primeiroNumero / segundoNumero;

print("dividindo os números se obtem : ", calculo)

calculo = primeiroNumero ** segundoNumero;

print("exponenciando os números se obtem : ", calculo)

usuarioDigitaNumero = int(input("digite um numero com pelo menos 2 casas decimais : "))

usuarioDigitaOutroNumero = int(input("digite outro numero : "))

calculo = usuarioDigitaNumero * usuarioDigitaOutroNumero / 100

print(usuarioDigitaOutroNumero, " % de ", usuarioDigitaNumero, " é ", calculo)