from random import choice
from colorama import Fore, Style, init
from time import sleep

# Inicialização do Colorama
init(autoreset=True)

# Divisória estilizada em Ciano Escuro
separador = Fore.CYAN + '=' * 50

# Título Principal
print(f'\n{separador}\n{Style.BRIGHT + Fore.YELLOW + "🎮 PEDRA, PAPEL E TESOURA 🎮"}\n{separador}')

valores = ['pedra', 'papel', 'tesoura']

while True:
    # Menu Principal
    print(f'''
{Style.BRIGHT + Fore.CYAN}--- MENU PRINCIPAL ---{Style.RESET_ALL}

{Fore.WHITE}[ 1 ] {Fore.GREEN}🎮 Iniciar o jogo
{Fore.WHITE}[ 2 ] {Fore.BLUE}📕 Como jogar?
{Fore.WHITE}[ 3 ] {Fore.RED}🚪 Sair  
''')
    
    resp = int(input('Escolha: '))
    print()
    print(separador)

    if resp == 1:
        while True:

            maquina = choice(valores)

            print(f'''\n{Fore.WHITE}[ 1 ] 🪨  Pedra
[ 2 ] ✋ Papel
[ 3 ] ✂️  Tesoura''')
            jogador = input('Escolha Pedra, Papel ou Tesoura: ').lower().strip()

            print(separador)

            if jogador.isnumeric():
                jogador = int(jogador)
                jogador = valores[jogador - 1]

            # Exibição de escolhas com cores em destaque
            print(f'Você: {Fore.CYAN + Style.BRIGHT + jogador.capitalize()} {Fore.WHITE}| Maquina: {Fore.MAGENTA + Style.BRIGHT + maquina.capitalize()}\n')
            
            # Mensagens de resultado
            if maquina == jogador:
                print(Fore.YELLOW + Style.BRIGHT + '🤝 Empate!')
            elif (
                (jogador == 'papel' and maquina == 'pedra') or
                (jogador == 'pedra' and maquina == 'tesoura') or
                (jogador == 'tesoura' and maquina == 'papel')
            ):
                print(Fore.GREEN + Style.BRIGHT + '🎉 VOCÊ VENCEU! 🎉')
            else:
                print(Fore.RED + Style.BRIGHT + '❌ VOCÊ PERDEU! ❌')

            print(separador)
            break

    elif resp == 2:

        # Tela de regras padronizada com o estilo do jogo
        print(Style.BRIGHT + Fore.CYAN + "📜 REGRAS DO JOKENPÔ\n")
        print(f"{Fore.WHITE}- Pedra ganha da Tesoura e perde pro Papel")
        print(f"{Fore.WHITE}- Papel ganha da Pedra e perde pra Tesoura")
        print(f"{Fore.WHITE}- Tesoura ganha do Papel e perde pra Pedra")
        print(Fore.YELLOW + "- Escolhas iguais = Empate!")
        print(separador)

    elif resp == 3:
        print(Fore.YELLOW + 'Saindo...')
        sleep(1)
        print(Fore.GREEN + 'Volte sempre! 👋')
        break
    else:
        print(Fore.RED + 'Opção inválida, tente novamente!')