from random import choice
from colorama import Fore, Style, init

separador = '=' * 45

# Inicialização do colorama
init(autoreset=True)

# Palavras 
palavras = ['PSICOLOGIA', 'PARADOXO', 'GIRASSOL', 'MOCHILA', 'ALGORITMO',
            'TERMINAL', 'XADREZ', 'PYTHON']

escolha = list(choice(palavras))
acertos = ['_'] * len(escolha)

tentativas = 0

# Lista de letras repetidas
repetidas = []

# Título
print(separador)
print(Fore.CYAN + 'JOGO DA FORCA'.center(20))
print(separador)

while True:
    letra = input('Letra: ').upper().strip()

    # Tratamento de erros de número
    if letra.isnumeric():
        continue
    
    # Tratamento de letras repetidas
    if letra in repetidas:
        print(Fore.LIGHTYELLOW_EX + 'Você já tentou essa letra')
        continue
    else:
        repetidas.append(letra)

    # Análise das letras
    if letra in escolha:
        for p, v in enumerate(escolha):
            if letra == v:
                acertos[p] = v
    else:
        print(f'Não tem {Fore.RED + letra}')
        tentativas += 1
    for i in acertos:
        print(Fore.GREEN + i if i != '_' else i, end=' ')
    print()

    # Mensagens de resultado
    if acertos == escolha:
        print(separador)
        print(Fore.GREEN + '🎉 VOCÊ GANHOU! 🎉')
        break
    if tentativas == 4:
        print(separador)
        print(Fore.RED + '❌ VOCÊ PERDEU! ❌')
        print(f'A palavra era {Fore.CYAN + "".join(escolha)}')
        break
