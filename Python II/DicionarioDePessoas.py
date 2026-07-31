pessoa = {}

pessoa["nome"] = input("Digite o nome da pessoa: ")
pessoa["idade"] = int(input("Digite a idade da pessoa: "))
pessoa["cidade"] = input("Digite a cidade da pessoa: ")
pessoa["profissao"] = input("Digite a profissão da pessoa: ")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("--------------------------------")

pessoa["profissao"] = "Outra profissão"

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")