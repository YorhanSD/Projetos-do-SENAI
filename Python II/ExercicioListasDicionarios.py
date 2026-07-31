livros = []

quantidade = int(input("Quantos livros deseja adicionar: "))

for i in range(quantidade):
    titulo = input("Adicione o título do livro: ")
    autor = input("Adicione o autor do livro: ")
    ano = input("Adicione o ano do livro: ")

    biblioteca = {
        "Titulo": titulo,
        "Autor": autor,
        "Ano": ano
    }

    livros.append(biblioteca)
    print()

while True:
    for livro in livros:
        print("Título:", livro["Titulo"])
        print("Autor:", livro["Autor"])
        print("Ano:", livro["Ano"])
        print("_" * 40)

    pergunta = input("Deseja excluir algum livro? ")

    if pergunta.lower() == "sim":
        titulo = input("Digite o nome do título que deseja excluir: ")

        for livro in livros:
            if livro["Titulo"] == titulo:
                livros.remove(livro)
                print("Você excluiu:", titulo)
                break
        else:
            print("Livro não encontrado.")
    else:
        print("Saindo...")
        break
