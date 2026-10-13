print('---CALCULO DE IMC---\n')

peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))

IMC = peso / (altura * altura)


if IMC < 18.5:
    print('Você está abaixo do peso normal')

elif IMC < 24.9:
    print('Você está com peso normal')

elif IMC < 29.9:
    print('Voce está com exesso de peso')

elif IMC < 34.9:
    print('Você esta com Obesidade clase I')

elif IMC < 39.9:
    print('Você está com Obesidade clase II')

elif IMC > 39.9:
    print('Obesidade clase III')






































































