digiteAltura = float(input("Digite sua altura : "))
digitePeso  = float(input("Digite seu peso : "))

imc = digitePeso / digiteAltura ** 2

print(f"O seu imc é : {imc: .2f}")

if(imc < 17):
    print("Muito baixo")
elif(imc > 17 and imc < 18.5):
    print("Baixo")
elif(imc > 18.5 and imc < 25):
    print("Peso ideal")
elif(imc > 25 and imc < 30):
    print("Acima do peso")
elif(imc > 30 and imc < 35):
    print("Obesidade 1")
elif(imc > 40 and imc < 45):
    print("Obesidade 2")
elif(imc > 40):
    print("Obesidade 3")