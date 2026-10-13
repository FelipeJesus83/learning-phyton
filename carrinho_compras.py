print('Projetos com PHYTON')

produtos = ['pao' , 'biscoito' , 'bolacha' , 'suco' ,  'bolo']
preços =  [ 20, 10, 13, 5, 35]

carrinho = []
carrinho_preços = []

print(' ---- BEM VINDOS A LOJA ---- ')

print('Produtos disponiveis: pao, biscoito, bolacha, suco, bolo ')

escolha = input('Digite o nome do produto que deseja: ').strip().lower()

if escolha in produtos:
    posição = produtos.index(escolha)
    print('Seu produto  chamado '  + escolha +' foi adicionado com sucesso no seu carrinho')

    carrinho.append(produtos[posição])
    carrinho_preços.append(preços[posição])

    print('Seu produto foi adicionado com sucesso no carrinho!')

else:
    print('O produto não existe em noss  loja')


if len(carrinho) > 0:
    total = sum(carrinho_preços)

    if total > 100:
        print('Parabens! Sua compra atingiu mais de 100R$,você acabou de ganhar um cupom')

    else:
        print('Sem cupom')

    print(f'Total a pagar: R${total}')
else:
    print('Seu carrinho está vazio')

sair = input('Deseja sair? (Sim = 1)(Não = Não responda)')






    