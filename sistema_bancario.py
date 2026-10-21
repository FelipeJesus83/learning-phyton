class Endereco:
    def __init__(self,rua,numero,bairro,estado,cidade):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.estado = estado
        self.cidade = cidade

    def exibir(self):
        print(f'Rua: {self.rua}, Numero: {self.numero}, Bairro: {self.bairro}, Estado: {self.estado}, Cidade: {self.cidade}')

class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = None

    def adicionar_end(self):
        rua = input('Digite a rua: ').strip()
        numero = input('Digite o número: ').strip()
        bairro = input('Digite o bairro: ').strip()
        estado = input('Digite o estado: ').strip()
        cidade = input('Digite a cidade: ').strip()
        self.endereco = Endereco(rua,numero,bairro,estado,cidade)
        print('Endereço cadastrado com sucesso!')
        return self.endereco


    def exibir_dados(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, Idade: {self.idade}')
        if self.endereco is not None:
            {self.endereco.exibir()}
        else:
            print('Endereço ainda não foi cadastrado!')
            i = input('Deseja cadastralo? (s/n): ').lower().strip()
            if i != 's':
                return
            else:
                self.adicionar_end()


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf,matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.salario_bs = 3000


    def calcular_pagamento(self):
        return self.salario_bs 

class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf, matricula,bonus):
        super().__init__(nome, idade, cpf, matricula)
        self.bonus = bonus
    

    def senha_frt_gerente(self):
        act = False
        while act != True:
            senha = input('Digite sua senha: ')
            if len(senha) >= 10 and '1234567890' in senha:
                print('Senha Forte')
                senha = True 
            else:
                print('Senha Fraca')
                print('Digite uma senha mais forte com numeros e 10 caracteres no minímo!')
                    
    
    def calcular_pagamento(self):
        return self.salario_bs + self.bonus

class Conta(Pessoa):
    def __init__(self, nome, idade, cpf,cliente):
        super().__init__(nome, idade, cpf)
        self.cliente = cliente
        self.numero_cnt = 1001
        self._saldo = 0.0
        self.historico = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self):
        valor = float(input('Quanto você quer depositar: '))
        if valor > 0.0:
            self.historico.append(f'Depósito: R${valor:.2f}')
            self._saldo += valor
            print(f'Você fez um depósito de: R${valor:.2f}')
        else:
            print('Saldo insuficiente!')

    def sacar(self):
        scr = float(input('Quanto você quer sacar: '))
        if scr <= self.saldo:
            self._saldo -= scr
            print(f'Você sacou R${scr:.2f} da sua conta!')
            print(f'Saldo: R${self.saldo}')
        else:
            print('Saldo insuficiente')

    def extrato(self):
        print('== Extrato ==')
        print(f'Nome; {self.nome}')
        print(f'Numero da Conta: {self.numero_cnt}')
        print(f'Historico: {self.historico}')
        print(f'Saldo: {self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, nome, idade, cpf, cliente):
        super().__init__(nome, idade, cpf, cliente)
        self.cheque = 500

    def sacar(self):
        scr = float(input('Quanto você quer sacar: '))
        total_scr = scr + 2 #taxa do banco
        if total_scr <= (self.saldo + self.cheque):
            self._saldo -= total_scr
            print(f'Você sacou {scr:.2f} da sua conta!')
            self.historico.append(f'Saque de: R${scr:.2f} com taxa de R$2,0')
        else:
            print('Saldo insuficiente junto ao cheque especial!')

class ContaPoupanca(Conta):
    def __init__(self, nome, idade, cpf, cliente):
        super().__init__(nome, idade, cpf, cliente)
        self.taxa_jrs = 0.05

    def render_jrs(self):
        rendimento = self.saldo * self.taxa_jrs
        self._saldo += rendimento
        self.historico.append(f'Rendimento: R${rendimento:.2f}')
        print(f'Sua conta rendeu R${rendimento}! Seu saldo atual e de: R${self.saldo:.2f}')



def cadastro():
    nm = str(input('Digite seu nome: ')).title().strip()
    idd = int(input('Digite sua idade: '))
    cpf = int(input('Digite seu CPF (apenas numeros): '))
    p1 = Pessoa(nm,idd,cpf)
    print('Cadastro feito com sucesso!')
    dsj = input('Deseja cadastrar o endereço agora (s/n): ').lower().strip()
    if dsj == 's':
        p1.adicionar_end()
    else:
        print('Endereço não cadastrado!')
    return p1

def escolha(p1):
    print('== Conta ==')
    print('Conta Corrente - 1')
    print('Conta Poupança - 2')
    opc = int(input('Escolha: '))

    if opc == 1:
        conta =  ContaCorrente(p1.nome,p1.idade,p1.cpf,p1)
        print('Conta Corrente criada com sucesso!')
        return conta
    if opc == 2:
        conta =  ContaPoupanca(p1.nome,p1.idade,p1.cpf,p1)
        print('Conta Poupança criada com sucesso!')
        return conta

p1 = cadastro()
conta_atv = escolha(p1)

# Funcionário e Gerente pré-cadastrados no banco
f1 = Funcionario('Lucas Silva', 25, '111.222.333-44', matricula=101)
g1 = Gerente('Carlos Mendes', 42, '999.888.777-66', matricula=201, bonus=1500)
g1.senha = 'admin123'

while True:
    print('== BEM-VINDO AO BANCO ==')
    print('1 - Sou Cliente')
    print('2 - Sou Funcionário')
    print('3 - Sou Gerente')
    print('4 - Sair ')


    opc = int(input('Escolha: '))

    if opc == 1:
        while True:
            print('\n== BANCO DIGITAL ==')
            print('1 - Depositar')
            print('2 - Sacar')
            print('3 - Extrato')
            print('4 - Render Juros (Apenas Poupança)')
            print('5 - Ver Dados do Titular (Pessoa + Endereço)')
            print('6 - Sair')
            opc = int(input('Escolha uma opção: '))

            if opc == 1:
                conta_atv.depositar()
            elif opc == 2:
                    conta_atv.sacar()
            elif opc == 3:
                conta_atv.extrato()
            elif opc == 4:
                if isinstance(conta_atv,ContaPoupanca):
                    conta_atv.render_jrs()
                else:
                    print('Opção inválida! Sua conta é Corrente, não Poupança!')
            elif opc == 5:
                p1.exibir_dados()
            elif opc == 6:
                print('Obrigado por usar o Banco Digital, Adeus...')
                break
            else:
                print('Opção inválida!')

    elif opc == 2:
        mtc = int(input('Digite sua matricula: '))
        if mtc == f1.matricula:
            print(f'Olá, {f1.nome}! Seu salário é: R$ {f1.calcular_pagamento():.2f}')
        else:
            print('Matricula inválida!')

    elif opc == 3:
        mtc = int(input('Digite sua matricula: '))
        senha = input('Digite sua senha: ')

        if mtc == g1.matricula and senha == g1.senha:
            print(f'Olá, Gerente {g1.nome}! Seu salário total com bônus é: R$ {g1.calcular_pagamento():.2f}')
            if isinstance (conta_atv, ContaCorrente):
                nv = input('Deseja mudar o valor do cheque especial do cliente(s/n) :').lower().strip()
                if nv == 's':
                    novo_valor = float(input('Digite o novo valor do cheque especial: '))
                    if novo_valor <= 0:
                        print('Escolha um valor maior que zero!')
                    else:
                        conta_atv.cheque = novo_valor
                        print(f'Valor do cheque especial trocado para: {novo_valor:.2f}')
                else:
                    print('Operação cancelada! Valor do cheque especial mantido.')
            else:
                print('Aviso: A conta do cliente atual é Poupança, não possui cheque especial.')

        else:
            print('Matricula ou Senha inválidas')

    elif opc == 4:
        print('Obrigado por usar o Banco Digital! Adeus...')
        break

    else:
        print('Opção inválida')


                





        





    


        

    


    

        
            





        
            
        