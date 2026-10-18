class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.lista = []

    def inserir(self,produto):
        self.lista.append(produto)

    def listar(self):
        for produto in self.lista:
            print(f'Produto: {produto.nome}, Preço: {produto.preco}')

    def calcula(self):
        total = 0
        for produto in self.lista:
            total += produto.preco
        print(f'Total a pagar: {total}')
        return total

    def desconto(self,total):
        if total > 100:
            desconto = 0.1
            total -= (total * desconto) 
            print(f'Você gastou mais de R$100 e recebeu 10% de desconto! Valor Final: {total}')
        else:
            print('Você não atingiu R$100 para receber o desconto de 10%!')


    def remover(self,nome_rmv):
        for produto in self.lista:
            if produto.nome == nome_rmv:
                self.lista.remove(produto)
                print(f'{nome_rmv} removido do carrinho!')
        else:
            print(f'{nome_rmv} não está no carrinho!')
        
carrinho = Carrinho()
def adicionar(carrinho):
    prd = input('Digite o nome do produto: ').capitalize().strip()
    prc = int(input('Digite o preço do produto: '))
    dsj = input('Deseja adicionar esse produto ao seu carrinho(s/n): ').lower().strip()
    if dsj == 's':
        p = Produto(prd,prc)
        carrinho.inserir(p)
        print(f'{prd} adicionado ao carrinho com sucesso!')
    else:
        print('Voltando para o menu...')
    return carrinho

def rmv(carrinho):
    carrinho.listar()
    rmv = input('Qual nome do produto que deseja remover: ').capitalize().strip()
    carrinho.remover(rmv)
    

while True:
    print('== Ecommerce ==')
    print('1 - Adicionar Produto')
    print('2 - Remover Produto')
    print('3 - Listar Produtos ')
    print('4 - Calcular total')
    print('5 - Sair')

    opc = int(input('Escolha: '))

    if opc == 1:
        adicionar(carrinho)
    elif opc == 2:
        rmv(carrinho)
    elif opc == 3:
        carrinho.listar()
    elif opc == 4:
        total = carrinho.calcula()
        carrinho.desconto(total)
    elif opc == 5:
        break
    else:
        print('Opção inválida')


