print('----Gerenciador de Produtos----\n')

dic_produtos = {'Ipad': 5000, 'Iphone': 6000, 'Macbook': 7000, 'Fone': 300, 'relogio': 1300}
print(dic_produtos)

escolha = input('Qual produto você quer: ').capitalize().strip()

if escolha in dic_produtos:
    print(f'O produto {escolha} foi escolhido')
    qntos = int(input('Quantos produtos você quer: '))
    preço = (dic_produtos[escolha])
    total = preço * qntos
    print(f'O total e igual a: {total}')
    if total >= 5000:
        desconto =  total * 0.20
        total_desconto = total - desconto
    elif total >= 2000:
        desconto = total * 0.10
        total_desconto = total - desconto
    else:
        total_desconto = total
        print('Sem descontos')
    print(f'O total final; R${total_desconto:3}')

else:
    print('Produto não existente')


















