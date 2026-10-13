alunos = {'João': [7, 8, 9],'Maria': [9, 9, 10],'Pedro': [5, 6, 7]}


def adicionar_notas(alunos):
    nome = input('Qual seu nome: ').capitalize().strip()
    if nome in alunos:
        notas = float(input('Qual foi sua nota: '))
        alunos[nome].append(notas)
        print(f'Nota adicionada ao {nome}!')        
    else:
        print('Aluno não está no sistema')

def calcular_media(alunos):
    nome = input('Qual seu nome: ')
    if nome in alunos:
        nota = alunos[nome]
        soma = sum(nota)
        quantidade = len(nota)
        media = soma / quantidade
        print(f'A media do {nome} é {media}')
    else:
        print('aluno não cadastrado')

def listar_alunos(alunos):
    for aluno in alunos:
        nota = alunos[aluno]
        soma = sum(nota)
        quantidade = len(nota)
        media = soma / quantidade
        print(f'O aluno: {aluno} tem media:{media}')

def verificação(alunos):
    nome = input('Qual seu nome: ')
    if nome in alunos:
        nota = alunos[nome]
        soma = sum(nota)
        quantidade = len(nota)
        media = soma / quantidade
        if media >= 7:
            print(f'O aluno: {nome} foi aprovado')
        else:
            print(f'O aluno: {nome} foi reprovado')
        return media

while True:
    print('=== MENU ===')
    print('1 - Adicionar nota')
    print('2 - Calcular média')
    print('3 - Listar alunos')
    print('4 - Verificar aprovação')
    print('5 - Sair')

    desejo = int(input('Oque deseja fazer: '))

    if desejo == 1:
        adicionar_notas(alunos)
    elif desejo == 2:
        calcular_media(alunos)
    elif desejo == 3:
        listar_alunos(alunos)
    elif desejo == 4:
        verificação(alunos)
    elif desejo == 5:
        break
    else:
        print('Opção inválida')