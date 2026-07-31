temperatura = float(input("Digite uma temperatura em celcius: "))

def conversor (temperatura):
    kelvin = temperatura + 273
    print ("Essa temperatura em kelvin é : ", kelvin)
    fahrenheit = temperatura * 9/5 + 32
    print ("Essa temperatura em fahrenheit é : ", fahrenheit)

conversor(temperatura)