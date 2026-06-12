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

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'categoria': self.categoria,
            'preco': self.preco,
            'quantidade': self.quantidade,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(int(d['codigo']), d['nome'], d.get('categoria', ''), float(d['preco']), int(d['quantidade']))

    def __repr__(self):
        return f"[{self.codigo}] {self.nome} | {self.categoria} | R$ {self.preco:.2f} | qt={self.quantidade}"
