
dicionario = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26
}

def criptografar(dicionario):
        palavra = input('Diga uma palavra: ').upper().strip()
        numeros = []
        for letra in palavra:
            numero = dicionario[letra]
            numeros.append(numero)
        return numeros


while True:
    print('==== MENU ====')
    print('Criptografia em Numeros')
    print('Criptografar = 1')
    print('Sair = 2')

    opção = int(input('Oque deseja fazer: '))

    if opção == 1:
        criptografar(dicionario)
    elif opção == 2:
         break
    else:
        print('Opção inválida')
         

            