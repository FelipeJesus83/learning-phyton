print('Estrutura de Dados\n')

produtos = [
    {"id": 101, "nome": "Teclado Mecânico", "preco": 180.00, "quantidade": 12},
    {"id": 102, "nome": "Mouse Gamer", "preco": 120.00, "quantidade": 20},
    {"id": 103, "nome": "Headset", "preco": 250.00, "quantidade": 8},
    {"id": 104, "nome": "Monitor 24", "preco": 850.00, "quantidade": 5},
    {"id": 105, "nome": "Webcam", "preco": 180.00, "quantidade": 15},
    {"id": 106, "nome": "SSD 1TB", "preco": 500.00, "quantidade": 7},
    {"id": 107, "nome": "Memória RAM 16GB", "preco": 350.00, "quantidade": 10},
    {"id": 108, "nome": "Mousepad", "preco": 80.00, "quantidade": 25}
]

def listar(produtos):
    print(produtos)
    for produto in produtos:
        produo = produto['nome']
        preço = produto['preco']
        print(f'O produto: {produo} custa: R${preço}')

def buscar(produtos):
    print(produtos)
    codigo = int(input('Qual o codigo do produto que você quer comprar: '))
    for produto in produtos:
        id = produto['id']
        if id == codigo:
            print(produto)
            break
    else:
        print('O seu codigo não está em produtos')

def alterar(produtos):
    print(produtos)
    codigo = int(input('Qual o codigo do produto que você quer alterar: '))
    for produto in produtos:
        if codigo == produto['id']:
            oque = int(input('Oque você deseja alterar:(1 = nome)(2 = preço)(3 = quantidade) '))
            if oque == 1:
                produto['nome'] = input('Que nome você quer colcocar: ')
                print(produto)
            elif oque == 2:
                produto['preco'] = float(input('Por qual valor você quer trocar: '))
                print(produto)
            elif oque == 3:
                produto['quantidade'] = int(input('Qual o novo estoque: '))
                print(produto)
            else:
                print('Opção inexistente')  
            break          
    else:
        print('Codigo inválido')


def remoção(produtos):
    print(produtos)
    codigo = int(input('Qual o codigo do produto que você quer remover: '))
    for produto in produtos:
        id = produto['id']
        if codigo == id:
            produtos.remove(produto)
            print(f'O produto do id: {id} foi removido')
            break
    else:
        print('O id Não foi encontrado')

def estoque(produtos):
    print(produtos)
    codigo = int(input('Qual o codigo do produto que você quer alterar o estoque: '))
    quantidade = int(input('Qual a quantidade que entrou no estoque:  '))
    for produto in produtos:
        if codigo == produto['id']:
            total = produto['quantidade'] + quantidade
            produto['quantidade'] = total
            print('A nova mercadoria foi adicionada ao estoque')
            break
    else:
        print('Codigo inválido')

while True:
    print("1 - Listar produtos")
    print("2 - Buscar produto")
    print("3 - Alterar produto")
    print("4 - Remover produto")
    print("5 - Entrada de estoque")
    print("6 - Sair")

    escolha = int(input("O que deseja fazer: "))

    if escolha == 1:
        listar(produtos)
    elif escolha == 2:
        buscar(produtos)
    elif escolha == 3: 
        alterar(produtos)
    elif escolha == 4:
        remoção(produtos)
    elif escolha == 5:
        estoque(produtos)
    elif escolha == 6:
        break
    else:
        print('Opção invalida')
