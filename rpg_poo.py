class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.vida_m = vida
        self.ataque = ataque

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} foi atacado! Vida restante: {self.vida}/{self.vida_m}")

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}!")
        alvo.receber_dano(self.ataque)


class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        self.especial = 2
    def usar_especial(self, alvo):
        if self.especial > 0:
            self.especial -= 1
            print(f"{self.nome} usou GOLPE PESADO com a faca em {alvo.nome}!")
            alvo.receber_dano(self.ataque * 2)
        else:
            print(f'{self.nome} tentou usar GOLPE PESADO, mas já esgotou os usos dete combate!')


class Mago(Personagem):
    def __init__(self, nome, vida, ataque, mana):
        super().__init__(nome, vida, ataque)
        self.mana = mana

    def usar_especial(self, alvo):
        if self.mana >= 20:
            self.mana -= 10
            print(f"{self.nome} disparou um projétil arcano em {alvo.nome}! Mana restante: {self.mana}")
            alvo.receber_dano(self.ataque * 3)
        else:
            print(f"{self.nome} tentou usar magia, mas está sem mana!")


class Arqueiro(Personagem):
    def usar_especial(self, alvo):
        print(f"{self.nome} disparou flechas certeiras em {alvo.nome}!")
        alvo.receber_dano(self.ataque * 2)


class Monstro(Personagem):
    def atacar(self, alvo):
        print(f"{self.nome} rugiu e mordeu {alvo.nome} ferozmente!")
        alvo.receber_dano(self.ataque)


import random  

def criar_monstro():
    monstros_disponiveis = [
        Monstro("Cangaceiro Traíra", 40, 10),
        Monstro("Lobisomem do Sertão", 70, 18),
        Monstro("Coronel Sangrento", 120, 25)
    ] 

    return random.choice(monstros_disponiveis)   

nome = input('Digite o seu nome: ').capitalize().strip()

print("\n--- ESCOLHA SEU PERSONAGEM ---")
print("1 - Guerreiro (Vida: 120, Ataque: 25)(2 = Golpes Especiais)")
print("2 - Mago (Vida: 70, Ataque: 15, Mana: 50)")
print("3 - Arqueiro (Vida: 90, Ataque: 20)")

monstro = criar_monstro()



def combate(jogador,monstro):
    while jogador.vida > 0 and monstro.vida > 0:
        print('1 - Atacar')
        print('2 - Habilidade Especial')

        op = int(input('Como você quer atacar: '))

        if op == 1:
            if monstro.vida > 0 and jogador.vida > 0:
                jogador.atacar(monstro)
                if monstro.vida > 0:
                    monstro.atacar(jogador)
                else:
                    print(f'{jogador.nome} Venceu a batalha!')
            elif jogador.vida < 0:
                print(f'{jogador.nome} Perdeu a batalha!')
        elif op == 2:
            if monstro.vida > 0 and jogador.vida > 0:
                jogador.usar_especial(monstro)
                if monstro.vida > 0:
                    monstro.atacar(jogador)
                else:
                    print(f'{jogador.nome} Venceu a batalha!')
            elif jogador.vida <= 0:
                print(f'{jogador.nome} Perdeu a Batalha!')

        else:
            print('Opção Inválida')



op = int(input("Escolha: "))

 
if op == 1:
    jogador = Guerreiro(nome,120,25)
    print(f"\nHerói {jogador.nome} pronto para a aventura! Vida: {jogador.vida}/{jogador.vida_m} | Ataque: {jogador.ataque}")
    combate(jogador,monstro)

elif op == 2:
    jogador =  Mago(nome,70,15,25)
    print(f"\nHerói {jogador.nome} pronto para a aventura! Vida: {jogador.vida}/{jogador.vida_m} | Ataque: {jogador.ataque}")
    combate(jogador,monstro)

elif op == 3:
    jogador = Arqueiro(nome,90,20)
    print(f"\nHerói {jogador.nome} pronto para a aventura! Vida: {jogador.vida}/{jogador.vida_m} | Ataque: {jogador.ataque}")
    combate(jogador,monstro)
else:
    print('Opção invalida')

