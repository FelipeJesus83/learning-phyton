
contatos ={
    'João': '11999999999',
    'Maria': '21988888888',
    'Pedro': '85977777777'
}

def adicionar(contatos):
    nome = input('Qual seu nome: ').capitalize().strip()
    print('Seu nome foi cadastrado!')
    telefone = input('Digite seu telefone:')
    print('O seu telefone foi cadastrado com sucesso')
    contatos[nome] = telefone
    print('Suas informações foram adicionadas com sucesso')

def buscar(contatos):
    nome = input('Qual seu nome: ').capitalize().strip()
    if nome in contatos:
        telefone = contatos[nome]
        print(telefone)
    else:
        print('O nome não existe')

def listar(contatos):
    for nome in contatos:
        print(nome)
        print(contatos[nome])

def remover(contatos):
    nome = input('Qual seu nome: ').capitalize().strip()
    if nome in contatos:
        del contatos[nome]
    else:
        print('Esse nome não existe')

while True:
    print('=== MENU ===')
    print('1 = adicionar')
    print('2 = buscar')
    print('3 = listar')
    print('4 = remover')
    print('5 = sair')
    print(contatos)

    escolha = int(input('Oque deseja fazer: '))

    if escolha == 1:
        adicionar(contatos)
    elif escolha == 2: 
        buscar(contatos)
    elif escolha == 3:
        listar(contatos)
    elif escolha == 4:
        remover(contatos)
    elif escolha == 5:
        break
    else:
        print('Opção inexistente')




