# Criação de um dicionário vazio chamado 'produto'.
# Dicionários em Python são estruturas de dados compostas por pares chave-valor.
produto = {}

# Adicionando novas chaves ao dicionário.
produto["nome do produto"] = input("Digite o nome do produto: ")
produto["valor do produto"] = float(input("Digite o valor do produto: "))
produto["estoque do produto"] = int(input("Digite o estoque do produto: "))

# Percorre todos os pares chave-valor do dicionário usando o método items().
# A variável 'chave' recebe o nome da chave e 'valor' recebe o valor correspondente.
# O método items() retorna uma visão dos pares chave-valor de um dicionário.
# Cada elemento retornado é uma tupla (chave, valor), permitindo percorrer todos os itens do dicionário.
for chave, valor in produto.items():
   print(f"{chave}: {valor}")