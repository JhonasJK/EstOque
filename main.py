from produto import Produto
from estoque import Estoque
from arquivos import salvar_produtos, carregar_produtos

estoque = Estoque()
estoque.produtos = carregar_produtos()

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar Produto")
    print("2 - Editar Produto")
    print("3 - Remover Produto")
    print("4 - Buscar por Código")
    print("5 - Buscar por Nome")
    print("6 - Registrar Venda")
    print("7 - Listar Produtos")
    print("8 - Listar por Categoria")
    print("9 - Estoque Baixo")
    print("10 - Relatório de Preços")
    print("11 - Salvar")
    print("12 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código: "))
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        produto = Produto(codigo, nome, categoria, preco, quantidade)
        estoque.cadastrar_produto(produto)
        salvar_produtos(estoque.produtos)

    elif opcao == "2":
        codigo = int(input("Código do produto: "))
        estoque.editar_produto(codigo)
        salvar_produtos(estoque.produtos)

    elif opcao == "3":
        codigo = int(input("Código do produto: "))
        estoque.remover_produto(codigo)
        salvar_produtos(estoque.produtos)

    elif opcao == "4":
        codigo = int(input("Código: "))
        indice = estoque.buscar_por_codigo(codigo)

        if indice != -1:
            print(estoque.produtos[indice])
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        nome = input("Nome: ")
        resultados = estoque.buscar_por_nome(nome)

        if resultados:
            for produto in resultados:
                print(produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "6":
        codigo = int(input("Código: "))
        quantidade = int(input("Quantidade vendida: "))
        estoque.registrar_venda(codigo, quantidade)
        salvar_produtos(estoque.produtos)

    elif opcao == "7":
        estoque.listar_produtos()

    elif opcao == "8":
        categoria = input("Categoria: ")
        estoque.listar_por_categoria(categoria)

    elif opcao == "9":
        limite = int(input("Limite: "))
        estoque.estoque_baixo(limite)

    elif opcao == "10":
        estoque.relatorio_precos()

    elif opcao == "11":
        salvar_produtos(estoque.produtos)
        print("Dados salvos.")

    elif opcao == "12":
        salvar_produtos(estoque.produtos)
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")