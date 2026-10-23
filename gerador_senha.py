import random

def gr_senha():

    
    alfabeto = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    simbolos = ['!', '@', '#', '$', '%', '&', '*', '?', '-', '_', '+', '=']

    l = int(input('Quantas letras deve ter sua senha: '))
    a = int(input('Quantos simbolos sua senha deve ter: '))
    n = int(input('Quantos numeros sua senha deve ter: '))

    senha = []
    for _ in range(l):
        l_srt = random.choice(alfabeto)
        senha.append(l_srt)

    for _ in range(n):
        n_srt = random.choice(numeros)
        senha.append(n_srt)

    for _ in range(a):
        s_srt = random.choice(simbolos)
        senha.append(s_srt)

    random.shuffle(senha)
    senha_p = ''.join(senha)

    print(f'Senha Gerada: {senha_p}')   


while True:
        print('1 - Gerar Senha')
        print('2 - Sair')

        opc = input('Escolha: ')

        if opc.isdigit():
            if opc == '1':
                gr_senha()
            elif opc == '2':
                break
            else:
                raise ValueError('Erro: Digite 1 para Gerar Senha e 2 para Sair!')

        else:
            raise ValueError('Erro: Digite apenas numeros!')
            