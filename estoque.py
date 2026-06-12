class Estoque:
    def __init__(self):
        self.produtos = []

    def buscar_por_codigo(self, codigo):
        inicio = 0
        fim = len(self.produtos) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if self.produtos[meio].codigo == codigo:
                return meio
            elif self.produtos[meio].codigo < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1

        return -1

    def buscar_por_nome(self, nome):
        resultados = []

        for produto in self.produtos:
            if nome.lower() in produto.nome.lower():
                resultados.append(produto)

        return resultados

    def cadastrar_produto(self, produto):
        if self.buscar_por_codigo(produto.codigo) != -1:
            print("Código já cadastrado.")
            return

        self.produtos.append(produto)
        self.produtos.sort(key=lambda p: p.codigo)

        print("Produto cadastrado com sucesso.")

    def editar_produto(self, codigo):
        indice = self.buscar_por_codigo(codigo)

        if indice == -1:
            print("Produto não encontrado.")
            return

        produto = self.produtos[indice]

        produto.nome = input("Novo nome: ")
        produto.categoria = input("Nova categoria: ")
        produto.preco = float(input("Novo preço: "))
        produto.quantidade = int(input("Nova quantidade: "))

        print("Produto atualizado.")

    def remover_produto(self, codigo):
        indice = self.buscar_por_codigo(codigo)

        if indice == -1:
            print("Produto não encontrado.")
            return

        del self.produtos[indice]
        print("Produto removido.")

    def registrar_venda(self, codigo, quantidade):
        indice = self.buscar_por_codigo(codigo)

        if indice == -1:
            print("Produto não encontrado.")
            return

        produto = self.produtos[indice]

        if quantidade > produto.quantidade:
            print("Estoque insuficiente.")
            return

        produto.quantidade -= quantidade
        print("Venda registrada.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos:
            print(produto)

    def listar_por_categoria(self, categoria):
        encontrou = False

        for produto in self.produtos:
            if produto.categoria.lower() == categoria.lower():
                print(produto)
                encontrou = True

        if not encontrou:
            print("Nenhum produto nessa categoria.")

    def estoque_baixo(self, limite):
        encontrou = False

        for produto in self.produtos:
            if produto.quantidade < limite:
                print(produto)
                encontrou = True

        if not encontrou:
            print("Nenhum produto com estoque baixo.")

    def relatorio_precos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        barato = min(self.produtos, key=lambda p: p.preco)
        caro = max(self.produtos, key=lambda p: p.preco)

        print("Produto mais barato:")
        print(barato)

        print("\nProduto mais caro:")
        print(caro)

def cadastrar_produto(estoque):
    try:
        codigo = int(input("Código: "))
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        produto = Produto(codigo, nome, categoria, preco, quantidade)
        estoque.cadastrar_produto(produto)
    except ValueError as e:
        print(f"Erro: {e}")