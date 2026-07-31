livros=[
    {
        "Titulo":"Dom Casmurro",
        "Autor" : "Machado de Assis",
        "Ano" : 1899
    }
    ,
    {
        "Titulo" : "Dom Quixote",
        "Autor" : "Miguel de Cervantes",
        "Ano" : 1605
    }
    ,
    {
        "Titulo" : "O Conde de Monte Cristo",
        "Autor" : "Alexandre Dumas",
        "Ano" : 1844
    }
]

for livro in livros:
    print("Titulo : ", livro["Titulo"])
    print("Autor : ", livro["Autor"])
    print("Ano : ", livro["Ano"])
    print("_"*40)
