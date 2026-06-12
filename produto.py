class Produto:
    def __init__(self, codigo: int, nome: str, categoria: str, preco: float, quantidade: int):
        if not isinstance(codigo, int):
            raise ValueError('Codigo deve ser inteiro')
        if not nome:
            raise ValueError('Nome vazio')
        if preco is None or preco <= 0:
            raise ValueError('Preco deve ser positivo')
        if quantidade is None or quantidade < 0:
            raise ValueError('Quantidade nao pode ser negativa')

        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.quantidade = int(quantidade)

def validar_codigo(codigo):
    if len(codigo) != 8: 
        return False 
    if not codigo.isalnum(): 
        return False 
    return True
def codigo_unico(codigo, produtos):
    for produto in produtos:
        if produto.codigo == codigo:
            return False
    return True

def __repr__(self):
        return F"[{self.codigo}] {self.nome} - {self.categoria} - R${self.preco:.2f} - Quantidade: {self.quantidade}"