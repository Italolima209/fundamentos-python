from random import choice

while True:
    jogador = input('Escolha pedra, papel ou tesoura: ').lower().strip()
    maquina = choice(['pedra', 'papel', 'tesoura'])
 
    print(f'Você escolheu: {jogador} e a Maquina escolheu: {maquina}')
    if maquina == jogador:
        print('Empate!')
    elif (
        (jogador == 'papel' and maquina == 'pedra') or
        (jogador == 'pedra' and maquina == 'tesoura') or
        (jogador == 'tesoura' and maquina == 'papel')
    ):
        print('Você venceu!')
    else:
        print('Você perdeu!')

    continuar = input('Deseja continuar? (S/N) ').lower().strip()[0]
    if continuar == 'n':
        print('Valeu por jogar, volte sempre!')
        break