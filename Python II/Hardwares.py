produtos = {
    "Mouse" : 25,
    "Teclado" : 30,
    "SSD" : 30
}

produto = input("Informe o produto que deseja pesquisar ou s para sair: ")

while True:

    if(produto in produtos):
        print(f"O produto {produto} custa {produtos[produto]}")
    else:
        print("Produto não encontrado")

    produto = input("Informe o produto que deseja pesquisar ou s para sair: ")

    if(produto == "S" or produto == "s"):
        break;

print("Saindo...")