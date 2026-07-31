# Criação de uma tupla chamada 'dados' que armazena três strings. 
# Tuplas são imutáveis, ou seja, após criadas, seus valores não podem ser alterados.
dados = ("nome", "idade", "cidade")

# Criação de um dicionário chamado 'pessoa'. 
# Os nomes das chaves vêm dos elementos da tupla 'dados', 
# e os valores são definidos para cada chave.
pessoa = {
   dados[0]: "Marcos Vinicius Carreiro",  # chave: "nome", valor: "Marcos Vinicius Carreiro"
   dados[1]: 37,                          # chave: "idade", valor: 37
   dados[2]: "São Paulo",                 # chave: "cidade", valor: "São Paulo"
}

# Exibe no console o valor associado à chave "nome" no dicionário 'pessoa'
print(pessoa["nome"])

# Adiciona uma nova chave "profissão" ao dicionário 'pessoa', 
# atribuindo o valor digitado pelo usuário como valor associado à chave.
pessoa["profissão"] = input("Digite sua profissão: ")

# Altera o valor da chave "nome" no dicionário 'pessoa' pelo valor digitado pelo usuário.
pessoa["nome"] = input("Digite seu nome: ")

# Exibe o novo valor associado à chave "nome" no dicionário 'pessoa' após a alteração.
print(pessoa["nome"])
# Remove a chave "nome" do dicionário 'pessoa' usando o comando del
del pessoa["nome"]

# Tenta exibir o valor associado à chave "nome" após ter sido removida.
# Isso resultará em um erro KeyError, pois "nome" não existe mais no dicionário.
# print(pessoa["nome"])