# MINE GAME V2 CRIADO POR Leozindev_genius

from time import sleep
from random import randint

# Função para título do código
def Titulo_game(txt_t):
    print('\033[34m-=\033[m' * 20)
    print(f'\033[35m{f"{txt_t}":^40}\033[m')
    print('\033[34m-=\033[m' * 20)

# Função para ganhos
def Venceu(txt):
    print('\033[33m-\033[m' * 40)
    print(f'\033[4;32m{f"{txt}":^40}\033[m')
    print('\033[33m-\033[m' * 40)

# função para perdas
def Perdeu(txt):
    print('\033[33m-\033[m' * 40)
    print(f'\033[4;31m{f"{txt}":^40}\033[m')
    print('\033[33m-\033[m' * 40)

# Função para empates
def Empate(txt):
    print('\033[33m-\033[m' * 40)
    print(f'\033[4;33m{f"{txt}":^40}\033[m')
    print('\033[33m-\033[m' * 40)

# Função de linhas
def Linhas():
    print('\033[33m-\033[m' * 40)


# Título do código
Titulo_game('MINE-GAME-V2')

# Código principal
while True:    
    # Opções de games
    print('''             \033[32m[ 1 ] PAR OU IMPAR\033[m
             \033[32m[ 2 ] ACERTE O NÚMERO\033[m
             \033[32m[ 3 ] JOKENPO\033[m
             \033[32m[ 4 ] LOTERIA\033[m
             \033[32m[ 5 ] SAIR\033[m''')
    Linhas()

    # Escolhendo o game
    game = int(input('Escolha o que vai jogar: '))
    print('Entrando no game...')
    Linhas()
    sleep(2)

    if game == 5:
        print('Saindo...')
        sleep(2)

    # Funções de entradas dos games
    # Game PAR OU IMPAR
    elif game == 1:
        Titulo_game('PAR-OU-IMPAR')
        print(f'{"REGRAS":^40}')
        Linhas()

        # Regras do game
        print('1°Você digita um número. \n2°Depois escolha a opção PAR OU IMPAR. \n3°A maquina irá gerar um número. \n4°Para ganhar a soma dos números deve ser \na mesma da opção que escolheu.')
        Linhas()
        # Variaveis de ganhos e perdas
        ganhos = perdas = 0
        
        while True:
            # Pegando o número do jogador
            num_user = int(input('Digite o seu número: '))
            print('Gerando número da maquina...')
            sleep(2)

            # Pegando o número da maquina
            maquina = randint(1, 50)
            soma_nums = num_user + maquina
            Linhas()
            print('\033[32m[ 1 ] PAR [ 2 ] IMPAR\033[m')

            # Escolhendo PAR ou IMPAR
            escolha = int(input('Escolha a sua opção: '))
            print('Gerando resultado...')
            Linhas()
            sleep(2)

            # Resultados do game
            if soma_nums % 2 == 0 and escolha == 1:
                print(f'A maquina escolheu o número {maquina} \nSomando os valores ficam {soma_nums} \nSendo um número PAR.')
                Venceu('VENCEU')
                ganhos += 1

                # Opções para continuar ou sair do game
                print('\033[32m[ 1 ] SIM [ 2 ] NÂO\033[m')
                escolha = int(input('Deseja continuar jogando? '))
                Linhas()
                if escolha == 1:
                    continue
                elif escolha == 2:
                    # Gerando resultado do game
                    print('Calculando resultado...')
                    sleep(2)
                    print(f'Você ganhou {ganhos} vezes. \nE perdeu {perdas} vezes.')
                    Linhas()
                    break
            
            elif soma_nums % 2 == 1 and escolha == 2:
                print(f'A maquina escolheu o número {maquina} \nSomando os valores ficam {soma_nums} \nSendo um número IMPAR.')
                Venceu('VENCEU')
                ganhos += 1
                
                # Opções para continuar ou sair do game
                print('\033[32m[ 1 ] SIM [ 2 ] NÂO\033[m')
                escolha = int(input('Deseja continuar jogando? '))
                Linhas()
                if escolha == 1:
                    continue
                elif escolha == 2:
                    # Gerando resultado do game
                    print('Calculando resultado...')
                    sleep(2)
                    print(f'Você ganhou {ganhos} vezes. \nE perdeu {perdas} vezes.')
                    Linhas()
                    break

            elif soma_nums % 2 == 0 and escolha == 2:
                print(f'A maquina escolheu o número {maquina} \nSomando os valores ficam {soma_nums} \nSendo um número PAR.')
                Perdeu('PERDEU')
                perdas += 1
                
                # Opções para continuar ou sair do game
                print('\033[32m[ 1 ] SIM [ 2 ] NÂO\033[m')
                escolha = int(input('Deseja continuar jogando? '))
                Linhas()
                if escolha == 1:
                    continue
                elif escolha == 2:
                    # Gerando resultado do game
                    print('Calculando resultado...')
                    sleep(2)
                    print(f'Você ganhou {ganhos} vezes. \nE perdeu {perdas} vezes.')
                    Linhas()
                    break

            elif soma_nums % 2 == 1 and escolha == 1:
                print(f'A maquina escolheu o número {maquina} \nSomando os valores ficam {soma_nums} \nSendo um número IMPAR.')
                Perdeu('PERDEU')
                perdas += 1
                
                # Opções para continuar ou sair do game
                print('\033[32m[ 1 ] SIM [ 2 ] NÂO\033[m')
                escolha = int(input('Deseja continuar jogando? '))
                Linhas()
                if escolha == 1:
                    continue
                elif escolha == 2:
                    # Gerando resultado do game
                    print('Calculando resultado...')
                    sleep(2)
                    print(f'Você ganhou {ganhos} vezes. \nE perdeu {perdas} vezes.')
                    Linhas()
                    break
    # Game ACERTE O NÚMERO
    elif game == 2:
        Titulo_game('ACERTE-O-NÚMERO')
        print(f'{"REGRAS":^40}')
        Linhas()
        
        # Regras do game
        print('1°Escolha o modo de jogo. \n2°Escolha o seu número. \n3°Números de acordo com o modo de jogo.')
        Linhas()

        # Modos de jogo
        print('''             \033[32m[ 1 ] 0, 10\033[m
             \033[32m[ 2 ] 0, 100\033[m
             \033[32m[ 3 ] 0, 1000\033[m''')
        Linhas()

        # Escolhendo o modo de jogo
        modo = int(input('Qual modo de jogo irá jogar? '))
        
        # Variaveis de tentativas
        tentativas = 0

       
        if modo == 1:
            Titulo_game('0, 10')
            num_maquina = randint(0, 10)
            while True:
                # Escolhendo o seu número
                num_user = int(input('Escolha o seu número: '))
                tentativas += 1

                print('Gerando número da maquina...')
                sleep(2)

                # Resutados do game
                if num_maquina == num_user:
                    Venceu('VENCEU')
                    print('Gerando resultado...')
                    sleep(2)
                    Linhas()
                    print(f'Total de {tentativas} tentativas.')

                    # Opções de continuar no modo ou sair
                    print('\033[32m[ 1 ] CONTINUAR [ 2 ] SAIR\033[m')
                    escolha = int(input('Escolha a sua opção: '))

                    # Começando um novo jogo
                    if escolha == 1:
                        print('Começando nova rodada...')
                        sleep(2)
                        continue
                    
                    # Saindo do modo de jogo atual
                    elif escolha == 2:
                        print('Saindo do modo...')
                        sleep(2)
                        break
                
                # Mensagem dizendo que o número sorteado e maior 
                elif num_maquina > num_user:
                    tentativas += 1 # Acrescentando mais uma tentativa
                    print(f'ACIMA DE {num_user}')
                    continue
                
                # Mensagem dizendo que o número sorteado e menor
                elif num_maquina < num_user:
                    tentativas += 1 # Acrescentando mais uma tentativa
                    print(f'ABAIXO DE {num_user}')
                    continue

        elif modo == 2:
            Titulo_game('0, 100')
            num_maquina = randint(0, 100)
            while True:
                # Escolhendo o seu número
                num_user = int(input('Escolha o seu número: '))
                tentativas += 1

                print('Gerando número da maquina...')
                sleep(2)

                # Resultado do game
                if num_maquina == num_user:
                    Venceu('VENCEU') 
                    print('Gerando resultado...')              
                    sleep(2)
                    Linhas()
                    print(f'Total de {tentativas} tentativas.')

                    # Opções de continuar no modo ou sair
                    print('\033[32m[ 1 ] CONTINUAR [ 2 ] SAIR\033[m')
                    escolha = int(input('Escolha a sua opção: '))

                    # Começando um novo jogo
                    if escolha == 1:
                        print('Começando nova rodada...')
                        sleep(2)
                        continue

                    # Saindo do modo de jogo atual
                    elif escolha == 2:
                        print('Saindo do modo...')
                        sleep(2)
                        break

                # Mensagem dizendo que o número sorteado e maior
                elif num_maquina > num_user:
                    tentativas += 1 # Acrescentando tentativas
                    print(f'ACIMA DE {num_user}')
                    continue

                # Mensagem dizendo que o número sorteado e menor
                elif num_maquina < num_user:
                    tentativas += 1 # Acrescentando tentativas
                    print(f'ABAIXO DE {num_user}')
                    continue

        elif modo == 3:
            Titulo_game('0, 1000')
            num_maquina = randint(0, 1000)
            while True:
                # Escolhendo o seu número
                num_user = int(input('Escolha o seu número: '))
                tentativas += 1

                print('Gerando número da maquina...')
                sleep(2)

                # Resultado do game
                if num_maquina == num_user:
                    Venceu('VENCEU')
                    print('Gerando resultado...')
                    sleep(2)
                    Linhas()
                    print(f'Total de {tentativas} tentativas.')

                    # Opções de continuar no modo ou sair
                    print('\033[32m[ 1 ] CONTINUAR [ 2 ] SAIR\033[m')
                    escolha = int(input('Escolha a sua opção: '))

                    # Começando um novo jogo
                    if escolha == 1:
                        print('Começando nova rodada...')
                        sleep(2)
                        continue

                    # Saindo do modo de jogo atual
                    elif escolha == 2:
                        print('Saindo do modo...')
                        sleep(2)
                        break

                # Mensagem dizendo que o número sorteado e maior
                elif num_maquina > num_user:
                    tentativas += 1 # Acrescentando tentativas
                    print(f'ACIMA DE {num_user}')
                    continue

                # Mensagem dizendo que o número sorteado e menor
                elif num_maquina < num_user:
                    tentativas += 1 # Acrescentando tentativas
                    print(f'ABAIXO DE {num_user}')
                    continue
    # Game JOKENPO
    elif game == 3:
        Titulo_game('JOKENPO')
        print(f'{"REGRAS":^40}')
        Linhas()
        
        # Variaveis do game
        empates = ganhos = perdas = 0

        # Regras o game
        print('1°Escolha a sua jogada. \n2°A maquina irá jogar. \n3°Você ganha pela lógica.')
        Linhas()

        while True:
            print('''             \033[32m[ 1 ] PEDRA\033[m
             \033[32m[ 2 ] PAPEL\033[m
             \033[32m[ 3 ] TESOURA\033[m''')
            Linhas()

            # Dicionario de jogadas
            jogadas = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}
            jogada = int(input('Escolha a sua jogada: ')) # Sua jogada
            maquina = randint(1, 3) # Jogada da maquina
            print('Maquina jogando...')
            Linhas()
            sleep(0.5)
            print(f'\033[31m{"JO":^13}\033[m', end='')
            sleep(0.5)
            print(f'\033[34m{"KEN":^15}\033[m', end='')
            sleep(0.5)
            print(f'\033[35m{"PO":^20}\033[m', end='\n')

            if jogada == maquina:
                empates += 1 # Acrecentando empates
                Empate('EMPATE')
                print(f'Sua jogada: {jogadas[jogada]}') # Mostrando a sua jogada
                print(f'Jogada da maquina: {jogadas[maquina]}') # Mostrando a jogada da maquina
                Linhas()
                continue            

            elif (jogada == 1 and maquina == 3) or (jogada == 2 and maquina == 1) or (jogada == 3 and maquina == 2):
                ganhos += 1 # Acrescentando ganhos
                Venceu('VENCEU')
                print(f'Sua jogada: {jogadas[jogada]}') # Mostrando a sua jogada
                print(f'Jogada da maquina: {jogadas[maquina]}') # Mostrando a jogada da maquina
                Linhas()

                # Opções de continuar no modo ou sair
                print('\033[32m[ 1 ] CONTINUAR [ 2 ] SAIR\033[m')
                escolha = int(input('Escolha a sua opção: '))

                # Começando um novo jogo
                if escolha == 1:
                    print('Começando nova rodada...')
                    sleep(2)
                    continue

                # Saindo do modo de jogo atual
                elif escolha == 2:
                    print('Saindo do modo...')
                    sleep(2)
                    break

            elif (maquina == 1 and jogada == 3) or (maquina == 2 and jogada == 1) or (maquina == 3 and jogada == 2):
                perdas += 1 # Acrescentando perdas
                Perdeu('PERDEU')
                print(f'Sua jogada: {jogadas[jogada]}') # Mostrando a sua jogada
                print(f'Jogada da maquina: {jogadas[maquina]}') # Mostrando jogada da maquina
                Linhas()

                # Opções de continuar no modo ou sair
                print('\033[32m[ 1 ] CONTINUAR [ 2 ] SAIR\033[m')
                escolha = int(input('Escolha a sua opção: '))

                # Começando um novo jogo
                if escolha == 1:
                    print('Começando nova rodada...')
                    sleep(2)
                    continue

                # Saindo do modo de jogo atual
                elif escolha == 2:
                    print('Saindo do modo...')
                    sleep(2)
                    break

    # Game LOTERIA
    elif game == 4:
        Titulo_game('LOTERIA')
        
        # Regras do game
        print(f'{"REGRAS":^40}')
        Linhas()
        print('1°Serão 10 números sorteados. \n2°Acerte no mínimo 7 números. \n3°Apenas números entre 0 e 65.')
        Linhas()

        # Coletando os números do usuário
        while True:
            user_nums = []
            for i in range(1, 11):
                while True:
                    try:
                        num = int(input(f'Digite o {i}° número: '))
                        if 1 <= num <= 65:
                            user_nums.append(num)
                            break
                        else:
                            print('\033[31mPor favor, insira um número entre 1 e 65.\033[m')
                    except ValueError:
                        print('\033[31mEntrada invalida. Digite um número inteiro.\033[m')
            
            # Sorteando os números
            sorted_nums = [randint(1, 65) for _ in range(15)]

            # Calculando acertos
            acertos = len(set(user_nums) & set(sorted_nums))

            Linhas()
            print('Sorteando números...')
            sleep(2)

            # Exibindo resultados
            Linhas()
            print(f'Seus números: ', sorted(user_nums))
            print(f'Números sorteados: ', sorted(sorted_nums))
            
            Linhas()
            # Acertos
            print(f'Você acertou \033[32m{acertos}\033[m números.')

            # Verificando se ganhou ou perdeu
            if acertos >= 7:
                Venceu('VENCEU')
            else:
                Perdeu('PERDEU')
            
            # Opções de continuar no modo ou sair
            print('\033[32m[ 1 ] CONTINUAR [ 2 ] SAIR\033[m')
            escolha = int(input('Escolha a sua opção: '))

            # Começando um novo jogo
            if escolha == 1:
                print('Começando nova rodada...')
                sleep(2)
                continue

            # Saindo do modo de jogo atual
            elif escolha == 2:
                print('Saindo do modo...')
                sleep(2)
                break
