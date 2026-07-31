#Dicionário é uma estrutura de dados que armazenas pares chave-valor.
#Cada elemento do dicionário consiste em uma chave e o valor associado a essa chave. 
#As chaves em um dicionario são únicas, ou seja, não podem existir chaves duplicadas.

#Um dicionário Python é uma coleção com elementos chave-valor que permite representar melhor o mundo real.

#Para criar um dicionário em Python utilizamos {}

# Criação de um dicionário chamado 'dic' contendo duas chaves:
# "curso" com valor "Python" e "professor" com valor "Anderson".
dic = {
    "curso": "Python",          # chave: "curso", valor: "Python"
    "professor": "Anderson"     # chave: "professor", valor: "Anderson"
}

# Exibe o dicionário completo no console.
print(dic)

# - Dentro das chaves {}, acessamos os valores das chaves no dicionário 'dic' diretamente.
# - dic["curso"] retorna o valor "Python".
# - dic["professor"] retorna o valor "Anderson".

print(f'O curso de {dic["curso"]} é ministrado pelo professor {dic["professor"]}')