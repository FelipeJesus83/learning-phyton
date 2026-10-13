print('Banco de Teste')
print('By felipe')

nome = str(input('Digite o seu nome inteiro: '))  
print(nome)
   
email= str(input('Digite o seu email inteiro: '))

print(email)

cpf = str(input('Digite seu CPF: '))

if len(cpf) != 11:
    print('CPF inválido')

else:
    print('CPF cadastrado com sucesso!')

numero_telefone = float(input('Digite o numero do seu telefone(COM O DDD): '))

mensagem1 = 'O seu numero de telefone foi cadastrado com sucesso!'

if numero_telefone > 9999999999999:
    print('Numero inválido')

else:
    print(mensagem1)

saldo = float(input('Digite seu saldo: '))

sim = 1
não = 2

if saldo <= 1000:
    print('Você está quebrado!!')
    emprego = int(input('Deseja um emprego? Sim = 1 Não = 2 '))

    if emprego  == 1 : 
        print('Você está contratatdo')
    
    elif emprego == 2:
         print('Você está fardado ao fracasso!')
    
    else:
        print('Opção inválida')
    
elif saldo >= 10000:
    print('Você está estavel!')
   


investimentos = float(input('Digite o dinheiro que você tem investido: '))
print(f'O seu total em investimentos é: {investimentos}')

if investimentos < 100:
    print('Você precisa investir mais!!')
    investir_melhor = int(input('Você quer aprender a investir? (sim = 1 não = 2): '))

    if investir_melhor == 1:
        print(f'O usuario chamado {nome} acabou de receber aulas de como investir no seu email que é {email}')

    elif investir_melhor == 2:
        print('Vai acabar endividado!')

    else:
        print('Opção inválida')


devendo = float(input('Qunto dinheiro você está devendo: '))
print(f'Suas dividas já somam: {devendo}')

if devendo > 1000:
    print('Você precisa quitar suas dividas!')
    dever_menos = int(input('Quer quitar suas dividas? (Sim = 1 , Não = 2) '))

    if dever_menos == 1:
        print(f'O usuario chamado {nome} recebeu uma mensagem no email onde ele recebera instruções para quitar sua dividas!!')

    elif dever_menos == 2:
        print('CUIDADO!! suas dividas são uma bola de neve')

    else:
        print('Opção invalida')

sair = input('Você deseja sair do sistema? (Sim = 1 )(Não = não responda)')

if sair == 1:
    print('Você saiu!')

