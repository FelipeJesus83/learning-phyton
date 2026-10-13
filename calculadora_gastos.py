
gastos = []

gasto1 = float(input('Quanto você gastou na primeira vez: '))
gastos.append(gasto1)

gasto2 = float(input('Quanto você gastou na segunda vez: '))
gastos.append(gasto2)

gasto3  = float(input('Quanto você gastou na terceira vez: '))
gastos.append(gasto3)

total_gastos = sum(gastos)

maior_gasto = max(gastos)

menor_gasto = min(gastos)

quantidade_gastos = len(gastos)
#EXIBIR
print(f'O total de gastos foi de: {total_gastos}')
print(f'O maior gasto foi de: {maior_gasto}')
print(f'O menor gasto foi: {menor_gasto}')
print(f'A quantidade de gastos foi de: {quantidade_gastos}')

contatos = []

nome1 = input('Diga o 1 nome: ')
contatos.append(nome1)

nome2 = input('Diga o 2 nome: ')
contatos.append(nome2)

nome3 = input('Diga o 3 nome: ')
contatos.append(nome3)

print('----------Nomes----------')
print(nome1.capitalize().strip())
print(nome2.capitalize().strip())
print(nome3.capitalize().strip())

quantidade = len(contatos)
posição = contatos.index(nome2)
print(f'A quantidade de contatos é: {quantidade}')
print(f'A posição do nome 2 é: {posição}')

contatos.remove(nome1)
print('Contatos após remover')
print(contatos)


































