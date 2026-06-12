# Sistema de Controle de Estoque

Projeto desenvolvido em Python para gerenciamento de estoque através do terminal (CLI).

## Integrantes

Gabriel Vitor :226696
João Pedro Matos: 211328
Mariana Oliveira de Souza: 236971

## Objetivo

O sistema permite realizar o controle de produtos em estoque, oferecendo funcionalidades de cadastro, busca, edição, remoção, vendas e relatórios.

## Funcionalidades

- Cadastrar produtos
- Editar produtos
- Remover produtos
- Buscar produto por código (Busca Binária)
- Buscar produto por nome (Busca Linear)
- Registrar vendas
- Listar produtos
- Filtrar produtos por categoria
- Relatório de estoque baixo
- Relatório de produtos mais caro e mais barato
- Salvar e carregar dados em JSON

## Estrutura do Projeto

```text
sistema-estoque/
│
├── main.py
├── produto.py
├── estoque.py
├── arquivos.py
├── produtos.json
└── README.md
```

## Tecnologias Utilizadas

- Python 3
- JSON
- Programação Orientada a Objetos (POO)

## Como Executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta do projeto

```bash
cd sistema-estoque
```

### 3. Executar o programa

```bash
python main.py
```

ou

```bash
python3 main.py
```

## Menu do Sistema

```text
1 - Cadastrar Produto
2 - Editar Produto
3 - Remover Produto
4 - Buscar por Código
5 - Buscar por Nome
6 - Registrar Venda
7 - Listar Produtos
8 - Listar por Categoria
9 - Estoque Baixo
10 - Relatório de Preços
11 - Salvar
12 - Sair
```

## Estrutura do Produto

Cada produto possui os seguintes atributos:

| Campo | Tipo |
|---------|---------|
| Código | Inteiro |
| Nome | String |
| Categoria | String |
| Preço | Float |
| Quantidade | Inteiro |

## Estrutura do Arquivo JSON

Exemplo:

```json
[
    {
        "codigo": 1,
        "nome": "Mouse",
        "categoria": "Periférico",
        "preco": 59.90,
        "quantidade": 20
    }
]
```

## Algoritmos Utilizados

### Busca Binária

Utilizada para localizar produtos através do código.

Características:

- Vetor ordenado por código
- Complexidade O(log n)
- Mais eficiente para pesquisas numéricas

### Busca Linear

Utilizada para localizar produtos pelo nome.

Características:

- Percorre todos os elementos
- Complexidade O(n)
- Permite busca parcial por texto

## Persistência de Dados

Os dados são armazenados no arquivo:

```text
produtos.json
```

Ao iniciar o sistema:

- Os produtos são carregados automaticamente.

Ao cadastrar, editar, remover ou vender:

- Os dados são salvos automaticamente.

## Exemplo de Uso

### Cadastro

```text
Código: 101
Nome: Mouse Gamer
Categoria: Periférico
Preço: 149.90
Quantidade: 15
```

### Venda

```text
Código: 101
Quantidade Vendida: 5
```

Resultado:

```text
Estoque Atual: 10
```

## Conceitos Aplicados

- Programação Orientada a Objetos
- Classes e Objetos
- Manipulação de Arquivos JSON
- Busca Binária
- Busca Linear
- Estruturas de Repetição
- Estruturas Condicionais
- Tratamento de Erros

## Licença

Projeto acadêmico desenvolvido para fins educacionais.