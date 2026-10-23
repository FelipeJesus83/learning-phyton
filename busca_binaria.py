class Busca:
    def __init__(self):
        self.lista = []
        self.alvo = None


    def adicionar_n(self):
        print('== Adicionar Numeros ==')
        qtd = int(input('Quantos numeros quer adicionar a lista: '))
        q = 0
        if isinstance(qtd, int):
            while q < qtd:
                q += 1
                n1 = int(input(f'Digite o {q}º numero: '))
                self.lista.append(n1)
                self.lista.sort()
                if q == qtd:
                    print(f'Lista Ordenada: {self.lista}')
                else:
                    continue
        else:
            raise ValueError('Erro: Digite apenas numeros inteiros!')
        
        acertou = False

        while acertou is not True:
            alvo = int(input('Qual o alvo para a Busca Binária: '))
            if alvo in self.lista:
                print('Alvo definidido!')
                acertou = True
                self.alvo = alvo
            else:
                print('Escolha um alvo que esteja na lista!')


    def buscar(self):
        print('== Busca Binária ==')
        alvo  = self.alvo
        i = 0
        f = len(self.lista) - 1
        t = 0
        while i <= f:
            t += 1 
            meio = (i + f) // 2
            if self.lista[meio] == alvo:
                print(f'Achou em {t} tentativas! Posição do alvo: {meio}.')
                break
            elif self.lista[meio] > alvo:
                f = meio - 1
            else:
                i = meio + 1

while True:
    b1 = Busca()
    print('1 - Busca Binária')
    print('2 - Sair')

    opc = input('Escolha: ')


    if opc.isdigit():
        if opc == '1':
            b1.adicionar_n()
            b1.buscar()
        elif opc == '2':
            break
        else:
            print('Numero inválido!')
    else:
        raise ValueError('Erro: Digite apenas numeros')