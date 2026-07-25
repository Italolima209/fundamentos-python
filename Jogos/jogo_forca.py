from random import choice

palavras = ['PSICOLOGIA', 'PARADOXO', 'GIRASSOL', 'MOCHILA', 'ALGORITMO',
            'TERMINAL', 'XADREZ', 'PYTHON']

escolha = list(choice(palavras))
acertos = ['_'] * len(escolha)

tentativas = 0

while tentativas < 3:

    letra = input('Letra: ').upper().strip()

    if letra not in escolha:
        tentativas += 1

    for p, v in enumerate(escolha):
        if letra == v:
            acertos[p] = v

    for i in acertos:
        print(i, end=' ')
    print()

    if acertos == escolha:
        print('Você ganhou')
        break
