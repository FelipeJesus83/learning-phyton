import random

jogador = {
    "nome": "",
    "vida": 100,
    "vida_max": 100,
    "ataque": 20,
    "ouro": 0,
    "inventario": []  
}

jogador['nome'] = input('Digite o nome do seu heroi: ').strip()

monstros = [
    {"nome": "Cangaceiro Traíra", "vida": 30, "ataque": 8, "ouro": 15},
    {"nome": "Lobisomem do Sertão", "vida": 60, "ataque": 15, "ouro": 35},
    {"nome": "Coronel Sangrento", "vida": 120, "ataque": 25, "ouro": 100}
]


pocoes = [
    {
        "nome": "Garrafada de Ervas",
        "tipo": "cura",
        "valor": 40,
        "descricao": "Cura 40 pontos de vida na hora."
    },
    {
        "nome": "Dose de Cachaça Braba",
        "tipo": "ataque",
        "valor": 10,
        "descricao": "Aumenta seu ataque permanente em +10."
    },
    {
        "nome": "Amuleto de Padre Cícero",
        "tipo": "vida_max",
        "valor": 25,
        "descricao": "Aumenta sua vida máxima em +25."
    }
]


def descansar(jogador):
    if jogador['vida'] >= jogador['vida_max']:
        print('Vida está cheia!')
    else:
        print(f"Você está ferido ({jogador['vida']}/{jogador['vida_max']})")
        qq = input('Você quer descansar(s/n): ').lower().strip()
        if qq != 's':
            print(f"Você não regenerou sua vida, sua vida atual é {jogador['vida']}/{jogador['vida_max']}")
        else:
            jogador['vida'] = min(jogador['vida_max'], jogador['vida'] + 20)
            print(f"Você descansou. Vida: {jogador['vida']}/{jogador['vida_max']}")


def status(jogador):
    print(f"Nome: {jogador['nome']}")
    print(f"Vida: {jogador['vida']}/{jogador['vida_max']}")
    print(f"Ataque: {jogador['ataque']}")
    print(f"Itens na Mochila: {len(jogador['inventario'])}")
    print(f"Ouro: {jogador['ouro']}")


def combate(jogador,monstros,pocoes):
    srt = random.choice(monstros).copy()
    print(f"Você achou o monstro {srt['nome']} com {srt['vida']} de vida!")
    while jogador['vida'] > 0 and srt['vida'] > 0:
        srt['vida'] = max(0, srt['vida'] - jogador['ataque'])
        print(f"{jogador['nome']} atacou o {srt['nome']}! O {srt['nome']} está com {srt['vida']} de vida")
        if srt['vida'] <= 0:
            print(f"Você derrotou o monstro {srt['nome']}")
            jogador['ouro'] += srt['ouro']
            print(f"Você roubou os ouros do {srt['nome']} e agora tem {jogador['ouro']} de ouro")
            pocao = random.choice(pocoes).copy()
            jogador['inventario'].append(pocao)
            print(f"Sua recopensa foi uma {pocao['nome']} de {pocao['tipo']}")
            break
        else:
            jogador['vida'] = max(0, jogador['vida'] - srt['ataque'])
            print(f"{jogador['nome']} foi atacado pelo {srt['nome']} e agora está com {jogador['vida']}/{jogador['vida_max']}")
            if jogador['vida'] <= 0:
                print('Você morreu,Fim de jogo')
                tnt = input('Quer tentar denovo (s/n): ').lower().strip()
                if tnt == 's':
                    reiniciar(jogador)
                    break
                else:
                    exit()


def reiniciar(jogador):
    jogador['vida_max'] = 100
    jogador['vida'] = 100
    jogador['ataque'] = 20
    jogador['ouro'] = 0
    jogador['inventario'] = []
    print('Personagem renacido,Todos os status foram resetados!')    


def mochila(jogador):
    if len(jogador['inventario']) == 0:
        print('Sua mochila está vazia. Consiga itens derrotando monstros ou na loja.')
        return

    for indice, item in enumerate(jogador['inventario']):
        print(f"{indice + 1} - {item['nome']}")

    print('0 - Voltar menu')
    entrada = input('O que deseja fazer/usar: ').strip()
    if not entrada.isdigit():
        print('Opção inválida!')
        return

    usar = int(entrada)
    if usar == 0:
        return
    elif 1 <= usar <= len(jogador['inventario']):
        item_usd = jogador['inventario'].pop(usar - 1)
        if item_usd['tipo'] == 'ataque':
            jogador['ataque'] += item_usd['valor']
            print(f"Você escolheu a poção de ataque! Seu ataque agora é de {jogador['ataque']}")
        elif item_usd['tipo'] == 'cura':
            jogador['vida'] = min(jogador['vida_max'], jogador['vida'] + item_usd['valor'])
            print(f"Você usou {item_usd['nome']}! Vida atual: {jogador['vida']}/{jogador['vida_max']}")
        elif item_usd['tipo'] == 'vida_max':
            jogador['vida_max'] += item_usd['valor']
            jogador['vida'] += item_usd['valor']
            print(f"Você usou {item_usd['nome']}! Vida máxima aumentada: {jogador['vida']}/{jogador['vida_max']}")
    else:
        print('Item inválido!')

    

def loja(jogador,pocoes):
    print("\n" + "=" * 40)
    print("      🏪 VENDA DO RPG (LOJA)")
    print("=" * 40)
    print(f"💰 Seu Ouro Atual: {jogador['ouro']} moedas\n")
    print("1 - Garrafada de Ervas (+40 Vida)       | Preço: 20 Ouro")
    print("2 - Dose de Cachaça Braba (+10 Ataque)   | Preço: 40 Ouro")
    print("3 - Amuleto de Padre Cícero (+25 VidaMax)| Preço: 60 Ouro")
    print("0 - Voltar ao Acampamento")
    print("=" * 40)
    entrada = input('Oque você quer comprar: ').strip()
    if not entrada.isdigit():
        print('Opção inválida!')
        return

    s = int(entrada)
    if s == 1:
        preco = 20
        if jogador['ouro'] >= preco:
            jogador['ouro'] -= preco
            jogador['inventario'].append(pocoes[0].copy())
            print(f"Você comprou {pocoes[0]['nome']} por {preco} de ouro!")
        else:
            print("Você não tem ouro suficiente!")
    elif s == 2:
        preco = 40
        if jogador['ouro'] >= preco:
            jogador['ouro'] -= preco
            jogador['inventario'].append(pocoes[1].copy())
            print(f"Você comprou {pocoes[1]['nome']} por {preco} de ouro!")
        else:
            print('Você não tem ouro suficiente!')
    elif s == 3:
        preco = 60
        if jogador['ouro'] >= preco:
            jogador['ouro'] -= preco
            jogador['inventario'].append(pocoes[2].copy())
            print(f"Você comprou {pocoes[2]['nome']} por {preco} de ouro!")
        else:
            print('Você não tem ouro suficiente!')
    elif s == 0:
        return
    else:
        print('Opção inválida')



while True:
    print("\n--- SERTÃO ROGUELIKE ---")
    print("1 - Explorar")
    print("2 - Mochila")
    print("3 - Descansar (+20 vida)")
    print("4 - Ver Status")
    print('5 - Reiniciar')
    print('6 - Loja RPG')
    print("7 - Sair")

    op = input("Escolha: ").strip()

    if op == "1":
        combate(jogador, monstros, pocoes)
    elif op == "2":
        mochila(jogador)
    elif op == "3":
        descansar(jogador)
    elif op == "4":
        status(jogador)
    elif op == "5":
        reiniciar(jogador)
    elif op == "6":
        loja(jogador, pocoes)
    elif op == '7':
        print('Saindo do jogo...')
        break
    else:
        print('Opção inexistente')
