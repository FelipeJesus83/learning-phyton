print('Calculo de vendas e meta de uma empresa')
print('By Felipe')

print('''TABELA DE BÔNUS:
- Vendas >= 15.000 + meta atingida = R$ 500
- Vendas >= 5.000 + meta atingida = R$ 100
- Vendas < 5.000 ou meta não atingida = sem bônus''')

vendas_empresa = float(input('Digite o total de vendas da empresa: '))
meta_empres = float(input('Qual a meta da empresa: '))
vendas_funcionario = float(input('Quanto de vendas um funcionario deve fazer: '))

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empres:
    bonus = 500
    print('Sua empresa bateu a meta!')
    print(f'O funcionario recebeu um bonus de {bonus}')

elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empres:
    bonus = 100
    print('Sua empresa bateu a meta!')
    print(f'Seu funcionario recebeu um bonus de {bonus}')

else:
    print('Sua empresa rendeu pouco e seu funcionario não recebeu bonus')

sair = input('Deseja sair? (Sim = 1) (Não = NÃO RESPONDA): ')