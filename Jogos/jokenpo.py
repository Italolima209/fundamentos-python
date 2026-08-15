from random import choice
from colorama import Fore, Style, init
from time import sleep

# Inicialização do Colorama
init(autoreset=True)

# Divisória estilizada
separador = Fore.CYAN + '=' * 50
valores = ['pedra', 'papel', 'tesoura']

def regras():
    print(Style.BRIGHT + Fore.CYAN + "📜 REGRAS DO JOKENPÔ\n")
    print(f"{Fore.WHITE}- Pedra ganha da Tesoura e perde pro Papel")
    print(f"{Fore.WHITE}- Papel ganha da Pedra e perde pra Tesoura")
    print(f"{Fore.WHITE}- Tesoura ganha do Papel e perde pra Pedra")
    print(Fore.YELLOW + "- Escolhas iguais = Empate!\n")
    print(separador)

def sair():
    print(Fore.YELLOW + 'Saindo...')
    sleep(1)
    print(Fore.GREEN + 'Volte sempre! 👋')

def jogar():
    while True:
        maquina = choice(valores)

        print(f'''\n{Fore.WHITE}[ 1 ] 🪨  Pedra
[ 2 ] ✋ Papel
[ 3 ] ✂️  Tesoura''')
        entrada = input('Escolha Pedra, Papel ou Tesoura: ').lower().strip()

        # Validação se digitou número
        if entrada.isnumeric():
            num = int(entrada)
            if 1 <= num <= 3:
                jogador = valores[num - 1]
            else:
                print(Fore.RED + 'Opção numérica inválida! Escolha 1, 2 ou 3.')
                continue
        elif entrada in valores:
            jogador = entrada
        else:
            print(Fore.RED + 'Entrada inválida! Digite Pedra, Papel, Tesoura ou o número correspondente.')
            continue

        print(separador)

        # Temporizador
        print('JO...')
        sleep(0.5)
        print('KEN...')
        sleep(0.5)
        print('PO!!\n')

        # Exibição de escolhas
        print(f'Você: {Fore.CYAN + Style.BRIGHT + jogador.capitalize()} {Fore.WHITE}| Máquina: {Fore.MAGENTA + Style.BRIGHT + maquina.capitalize()}\n')
        
        # Resultado
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

# Título Principal
print(f'\n{separador}\n{Style.BRIGHT + Fore.YELLOW + "🎮 PEDRA, PAPEL E TESOURA 🎮".center(50)}\n{separador}')

# Loop do Menu Principal
while True:
    print(f'''
{Style.BRIGHT + Fore.CYAN}--- MENU PRINCIPAL ---{Style.RESET_ALL}

{Fore.WHITE}[ 1 ] {Fore.GREEN}🎮 Iniciar o jogo
{Fore.WHITE}[ 2 ] {Fore.BLUE}📕 Como jogar?
{Fore.WHITE}[ 3 ] {Fore.RED}🚪 Sair  
''')
    
    opcao = input('Escolha uma opção: ').strip()
    print(separador)

    if opcao == '1':
        jogar()
    elif opcao == '2':
        regras()
    elif opcao == '3':
        sair()
        break
    else:
        print(Fore.RED + 'Opção inválida, tente novamente!')