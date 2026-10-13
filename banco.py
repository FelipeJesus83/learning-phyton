print('==========')
print('Banco by Felipe')
print('==========')
print('Saldo ')
print('Investimentos ')
print('Dividas ')
print('Transações')
print('==========')

def verificar_email(email):
    if '@gmail.com' in email or '@hotmail.com' in email:
        print('Seu email está correto')
    else:
        print('Seu email está incompleto')
        
email = input('Digite seu email: ').lower().strip()
ver_email = verificar_email(email)

# 1000 no saldo 200 investido = pouco investimento
 
saldo = float(input('Digite seu saldo:'))
print(f'O seu saldo e de {saldo}')
investimentos = float(input('Quanto você tem investido: '))


def investimentos_de_acordo_saldo(saldo, investimentos):
    if investimentos > saldo:
        print('Você não tem mais investimentos que saldo')
    else:   
       if saldo % 3 < investimentos:
        mais = input('Deseja investir mais: ').lower().strip() 
        if mais == 'sim':
            print(f'Você recebeu um curso GRATIS no seu email: {email}')
        elif mais == 'nao' or mais == 'não':
           print('Você foi avisado!!')
        else:
             print('Opção invalida')
       else:
        print('Seu investimentos estão bons!')

investimentos_de_acordo_saldo(saldo, investimentos)

dividas = int(input('Quanto você está devendo: '))
def calculo_dividas(dividas, saldo):
    if dividas > (saldo * 2 ):
      print('Suas dividas sao o dobro')
    elif dividas > (saldo * 3):
      print('Suas dividas estão o triplo do seu Saldo!!')
    elif dividas < saldo:
       deseja = input('Deseja quitar suas dividas: ').lower().strip()
       if deseja == 'sim':
          print('Suas dividas foram quitadas') 
       elif deseja == 'nao' or deseja == 'não':
          print('Suas dividas não foram quitadas')
       else:
          print('Opção inválida')

calculo_dividas(dividas, saldo)
   

historico = []

def registrar_transação(investimentos,saldo,dividas):
   historico.append(f'Investimentos: {investimentos}')
   historico.append(f'Saldo; {saldo}')
   historico.append(f'Dividas{dividas}')
   print(f'Seu historico: {historico}')

def mostrar_historico():
   for transação in historico:
      print(transação)

registrar_transação(investimentos,saldo,dividas)
mostrar_historico()















































