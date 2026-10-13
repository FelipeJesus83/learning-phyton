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

sair = input('Deseja sair? Sim = 1 Não = não responda ')