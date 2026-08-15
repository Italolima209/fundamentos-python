from random import choice
from colorama import Fore, init

separador = '=' * 45

# Inicialização do colorama
init(autoreset=True)

def formaboneco(erros):
    estagios = {
        1: '  ( )',
        2: '  ( )\n   |\n   |',
        3: '  ( )\n \\ | \n   |',
        4: '  ( )\n \\ | /\n   |',
        5: '  ( )\n \\ | /\n   |\n  / ',
        6: '  ( )\n \\ | /\n   |\n  / \\'
    }
    if erros in estagios:
        print(estagios[erros])

# Palavras
palavras = [
    'PSICOLOGIA', 'PARADOXO', 'GIRASSOL', 'MOCHILA', 
    'ALGORITMO', 'TERMINAL', 'XADREZ', 'PYTHON', 'CACHORRO'
]

escolha = list(choice(palavras))
acertos = ['_'] * len(escolha)
tentativas = 0
repetidas = []

# Título
print(separador)
print(Fore.CYAN + 'JOGO DA FORCA'.center(45))
print(separador)

while True:
    letra = input('\nDigite uma letra: ').upper().strip()

    # Validação: apenas uma única letra do alfabeto
    if len(letra) != 1 or not letra.isalpha():
        print(Fore.YELLOW + 'Por favor, digite apenas uma única letra válida.')
        continue
    
    # Tratamento de letras repetidas
    if letra in repetidas:
        print(Fore.LIGHTYELLOW_EX + 'Você já tentou essa letra!')
        continue
    else:
        repetidas.append(letra)

    # Análise da letra
    if letra in escolha:
        for p, v in enumerate(escolha):
            if letra == v:
                acertos[p] = v
    else:
        print(f'Não tem a letra {Fore.RED + letra}')
        tentativas += 1
        if 6 - tentativas > 0:
            print(Fore.RED + f'Restam {6 - tentativas} tentativas.')

    # Estrutura do boneco
    formaboneco(tentativas)

    # Exibição do progresso
    print('\nPalavra: ', end='')
    for i in acertos:
        print(Fore.GREEN + i if i != '_' else i, end=' ')
    print()

    # Mensagens de resultado
    if acertos == escolha:
        print('\n' + separador)
        print(Fore.GREEN + '🎉 VOCÊ GANHOU! 🎉')
        print(separador)
        break

    if tentativas == 6:
        print('\n' + separador)
        print(Fore.RED + '❌ VOCÊ PERDEU! ❌')
        print(f'A palavra era: {Fore.CYAN + "".join(escolha)}')
        print(separador)
        break