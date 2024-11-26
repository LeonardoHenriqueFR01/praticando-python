# MINI GAMES CRIADO POR Leonardo Henrique

from time import sleep
from random import randint


print('\033[32m-=\033[m' * 20)
print(f'\033[34m{"MINI GAMES":-^40}\033[m')
print('\033[32m-=\033[m' * 20)

while True:
    print('\033[33m-\033[m' * 40)
    print('''                   \033[4;35mGAMES\033[m
                \033[36m[ 1 ] JOKENPO\033[m
                \033[33m[ 2 ] ACERTE O NÚMERO\033[m
                \033[32m[ 3 ] LOTERIA\033[m
                \033[34m[ 4 ] PAR OU IMPAR\033[m
                \033[31m[ 5 ] SAIR\033[m''')
    print('\033[33m-\033[m' * 40)

    opção =  int(input('QUAL JOGO VOCÊ DESEJA JOGAR: '))

    if opção == 1:
        print('ENTRANDO NO GAME...')
        sleep(2)
        print('\033[33m-\033[m' * 40)
        print(f'\033[36m{"JOKENPO":-^40}\033[m')
        print('\033[33m-\033[m' * 40)

        user = str(input('QUAL É O SEU NOME? '))

        ganhos = 0
        perdas = 0
        empates = 0

        while True:
            print('\033[33m-\033[m' * 40)
            print(f'\033[4;36m{"ESCOLHA A SUA JOGADA":^40}\033[m')
            print('\033[33m-\033[m' * 40)
            print('''                \033[32m[ 1 ] PEDRA\033[m
                \033[32m[ 2 ] PAPEL\033[m
                \033[32m[ 3 ] TESOURA\033[m
                \033[31m[ 4 ] SAIR\033[m''')
            list_jogadas = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}

            jogada = int(input(f'{user} ESCOLHA A SUA JOGADA: '))
            maquina = randint(1, 3)

            if jogada == maquina:
                empates += 1
                print('MAQUINA JOGANDO...')
                print('\033[33m-\033[m' * 40)
                sleep(2)
                print(f'\033[35m{"JO":^40}\033[m')
                sleep(0.5)
                print(f'\033[35m{"KEN":^40}\033[m')
                sleep(0.5)
                print(f'\033[35m{"POO!":^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'\033[33m{"EMPATE":^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'\033[32mSUA JOGADA: {list_jogadas[jogada]}\033[m')
                print(f'\033[31mJOGADA DA MAQUINA: {list_jogadas[maquina]}\033[m')

            elif (jogada == 1 and maquina == 3) or (jogada == 2 and maquina == 1) or (jogada == 3 and maquina == 2):
                print('MAQUINA JOGANDO...')
                print('\033[33m-\033[m' * 40)
                sleep(2)
                print(f'\033[35m{"JO":^40}\033[m')
                sleep(0.5)
                print(f'\033[35m{"KEN":^40}\033[m')
                sleep(0.5)
                print(f'\033[35m{"POO!":^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'\033[32m{"VOCE GANHOU":^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'\033[32mSUA JOGADA: {list_jogadas[jogada]}\033[m')
                print(f'\033[31mJOGADA DA MAQUINA: {list_jogadas[maquina]}\033[m')
                ganhos += 1

            elif (maquina == 1 and jogada == 3) or (maquina == 2 and jogada == 1) or (maquina == 3 and jogada ==2):
                print('MAQUINA JOGANDO...')
                print('\033[33m-\033[m' * 40)
                sleep(2)
                print(f'\033[35m{"JO":^40}\033[m')
                sleep(0.5)
                print(f'\033[35m{"KEN":^40}\033[m')
                sleep(0.5)
                print(f'\033[35m{"POO!":^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'\033[31m{"MAQUINA VENCEU":^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'\033[32mSUA JOGADA: {list_jogadas[jogada]}\033[m')
                print(f'\033[31mJOGADA DA MAQUINA: {list_jogadas[maquina]}\033[m')
                perdas += 1

            elif jogada != 1 and jogada != 2 and jogada != 3 and jogada != 4:
                print('JOGADA INVÁLIDA TENTE NOVAMENTE...')
                sleep(2)
            
            elif jogada == 4:
                print('FINALIZANDO...')
                sleep(2)
                print('CALCULANDO RESULTADO...')
                sleep(2)
                print('\033[33m-\033[m' * 40)
                print(f'{user} VOCÊ GANHOU: {ganhos} VEZES!')
                print(f'PERDEU {perdas} VEZES!')
                print(f'EMPATOU {empates} VEZES!')
                break

    elif opção == 2:
        print('ENTRANDO NO GAME...')
        sleep(2)
        print('\033[33m-\033[m' * 40)
        print(f'\033[36m{"ACERTE O NÚMERO":-^40}\033[m')
        print('\033[33m-\033[m' * 40)

        user = str(input('QUAL É O SEU NOME? '))

        while True:
            print('''AQUI ESTÃO AS OPÇÕES
                \033[32m[ 1 ] 1, ATÉ 10\033[m
                \033[32m[ 2 ] 10, ATÉ 100\033[m
                \033[32m[ 3 ] 100 ATÉ 1000\033[m
                \033[31m[ 4 ] SAIR\033[m''')
            print('\033[33m-\033[m' * 40)

            modo = int(input(f'{user}, QUAL É A SUA OPÇÃO: '))
            if modo == 4:
                print("SAINDO DO GAME...")
                sleep(2)
                break

            tentativas = 0

            if modo == 1:
                maquina = randint(1, 10)
                print('ENTRANDO NO MODO...')
                sleep(2)
                print('\033[33m-\033[m' * 40)

                while True:
                    print(f'\033[34m{"ACERTE O NÚMERO DE 1 ATÉ 10":-^40}\033[34m')
                    print('\033[33m-\033[m' * 40)
                    num_user = int(input('DIGITE O SEU NÚMERO: '))
                    tentativas += 1
                    print('GERANDO NÚMERO...')
                    sleep(2)

                    if num_user == maquina:
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32m{"VOCÊ GANHOU":-^40}\033[m')
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32mSEU NÚMERO FOI: {num_user}!\033[m')
                        print(f'\033[31mNÚMERO SORTEADO FOI: {maquina}!\033[31m')
                        print('\033[33m-\033[m' * 40)
                        print('''AQUI ESTÃO AS OPÇÕES
                \033[32m[ 1 ] CONTINUAR\033[m
                \033[31m[ 2 ] SAIR/RESULTADO\033[m''')
                        print('\033[33m-\033[m' * 40)
                        modo = int(input(f'{user} QUAL É A SUA OPÇÃO: '))

                        if modo == 1:
                            # Gera um novo número para a próxima rodada
                            maquina = randint(1, 10)
                            tentativas = 0  # Reinicia a contagem de tentativas
                        elif modo == 2:
                            print('SAINDO DO GAME...')
                            sleep(1)
                            print('GERANDO RESULTADO...')
                            sleep(2)
                            print('\033[33m-\033[m' * 40)
                            print(f'{user}, VOCÊ TEVE UM TOTAL DE {tentativas} TENTATIVAS!')
                            break  # Sai do loop principal e encerra o jogo
                    else:
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[31m{"VOCÊ PERDEU":-^40}\033[31m')
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32mSEU NÚMERO FOI: {num_user}!\033[m')
                        if maquina > num_user:
                            print('MAIS... TENTE NOVAMENTE!')
                        else:
                            print('MENOS... TENTE NOVAMENTE!')
                        print('\033[33m-\033[m' * 40)

            if modo == 2:
                maquina = randint(10, 100)
                print('ENTRANDO NO MODO...')
                sleep(2)
                print('\033[33m-\033[m' * 40)

                while True:
                    print(f'\033[34m{"ACERTE O NÚMERO DE 10 ATÉ 100":-^40}\033[34m')
                    print('\033[33m-\033[m' * 40)
                    num_user = int(input('DIGITE O SEU NÚMERO: '))
                    tentativas += 1
                    print('GERANDO NÚMERO...')
                    sleep(2)

                    if num_user == maquina:
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32m{"VOCÊ GANHOU":-^40}\033[m')
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32mSEU NÚMERO FOI: {num_user}!\033[m')
                        print(f'\033[31mNÚMERO SORTEADO FOI: {maquina}!\033[31m')
                        print('\033[33m-\033[m' * 40)
                        print('''AQUI ESTÃO AS OPÇÕES
                \033[32m[ 1 ] CONTINUAR\033[m
                \033[31m[ 2 ] SAIR/RESULTADO\033[m''')
                        print('\033[33m-\033[m' * 40)
                        modo = int(input(f'{user} QUAL É A SUA OPÇÃO: '))

                        if modo == 1:
                            # Gera um novo número para a próxima rodada
                            maquina = randint(1, 10)
                            tentativas = 0  # Reinicia a contagem de tentativas
                        elif modo == 2:
                            print('SAINDO DO GAME...')
                            sleep(1)
                            print('GERANDO RESULTADO...')
                            sleep(2)
                            print('\033[33m-\033[m' * 40)
                            print(f'{user}, VOCÊ TEVE UM TOTAL DE {tentativas} TENTATIVAS!')
                            break  # Sai do loop principal e encerra o jogo
                    else:
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[31m{"VOCÊ PERDEU":-^40}\033[31m')
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32mSEU NÚMERO FOI: {num_user}!\033[m')
                        if maquina > num_user:
                            print('MAIS... TENTE NOVAMENTE!')
                        else:
                            print('MENOS... TENTE NOVAMENTE!')
                        print('\033[33m-\033[m' * 40)

            if modo == 3:
                maquina = randint(100, 1000)
                print('ENTRANDO NO MODO...')
                sleep(2)
                print('\033[33m-\033[m' * 40)

                while True:
                    print(f'\033[34m{"ACERTE O NÚMERO DE 100 ATÉ 1000":-^40}\033[34m')
                    print('\033[33m-\033[m' * 40)
                    num_user = int(input('DIGITE O SEU NÚMERO: '))
                    tentativas += 1
                    print('GERANDO NÚMERO...')
                    sleep(2)

                    if num_user == maquina:
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32m{"VOCÊ GANHOU":-^40}\033[m')
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32mSEU NÚMERO FOI: {num_user}!\033[m')
                        print(f'\033[31mNÚMERO SORTEADO FOI: {maquina}!\033[31m')
                        print('\033[33m-\033[m' * 40)
                        print('''AQUI ESTÃO AS OPÇÕES
                \033[32m[ 1 ] CONTINUAR\033[m
                \033[31m[ 2 ] SAIR/RESULTADO\033[m''')
                        print('\033[33m-\033[m' * 40)
                        modo = int(input(f'{user} QUAL É A SUA OPÇÃO: '))

                        if modo == 1:
                            # Gera um novo número para a próxima rodada
                            maquina = randint(1, 10)
                            tentativas = 0  # Reinicia a contagem de tentativas
                        elif modo == 2:
                            print('SAINDO DO GAME...')
                            sleep(1)
                            print('GERANDO RESULTADO...')
                            sleep(2)
                            print('\033[33m-\033[m' * 40)
                            print(f'{user}, VOCÊ TEVE UM TOTAL DE {tentativas} TENTATIVAS!')
                            break  # Sai do loop principal e encerra o jogo
                    else:
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[31m{"VOCÊ PERDEU":-^40}\033[31m')
                        print('\033[33m-\033[m' * 40)
                        print(f'\033[32mSEU NÚMERO FOI: {num_user}!\033[m')
                        if maquina > num_user:
                            print('MAIS... TENTE NOVAMENTE!')
                        else:
                            print('MENOS... TENTE NOVAMENTE!')
                        print('\033[33m-\033[m' * 40)

    elif opção == 3:
        print('ENTRANDO NO GAME...')
        sleep(2)
        print('\033[33m-\033[m' * 40)
        print(f'\033[32m{"LOTERIA":-^40}\033[m')
        print('\033[33m-\033[m' * 40)
        user = input('QUAL É O SEU NOME? ')
        print('\033[33m-\033[m' * 40)

        print(f'REGRAS: SERÃO 15 NÚMEROS SORTEADOS \nNÚMEROS DE 1 ATÉ 65 \n{user} VOCÊ DEVE ACERTAR NO MÍNIMO 7!')
        print('\033[33m-\033[m' * 40)

        # Coletando os números do usuário
        while True:
            user_numbers = []
            for i in range(1, 16):
                while True:
                    try:
                        num = int(input(f'DIGITE O {i}° NÚMERO: '))
                        if 1 <= num <= 65:
                            user_numbers.append(num)
                            break
                        else:
                            print("\033[31mPor favor, insira um número entre 1 e 65.\033[m")
                    except ValueError:
                        print("\033[31mEntrada inválida. Digite um número inteiro.\033[m")

            # Sorteando os números
            sorted_numbers = [randint(1, 65) for _ in range(15)]

            # Calculando os acertos
            acertos = len(set(user_numbers) & set(sorted_numbers))

            print('\033[33m-\033[m' * 40)
            print(f'\033[35m{"SORTEANDO NÚMEROS...":^40}\033[m')
            sleep(2)

            # Exibindo resultados
            print('\033[33m-\033[m' * 80)
            print("\033[32mSEUS NÚMEROS: \033[m", sorted(user_numbers))
            print("\033[31mNÚMEROS SORTEADOS: \033[m", sorted(sorted_numbers))
            print('\033[33m-\033[m' * 80)
            print(f'{f"VOCÊ ACERTOU \033[32m{acertos}\033[m NÚMEROS.":-^48}')

            # Verificando se ganhou ou perdeu
            if acertos >= 7:
                print('\033[33m-\033[m' * 40)
                print(f'\033[32m{"PARABÉNS! VOCÊ GANHOU!":-^40}\033[32m')
            else:
                print('\033[33m-\033[m' * 80)
                print(f'\033[31m{"VOCÊ PERDEU. TENTE NOVAMENTE":-^40}\033[m')
            print('\033[33m-\033[m' * 40)

            continuar = str(input('DESEJA JOGAR NOVAMENTE? (s/n): ')).strip().lower()
            
            if continuar != 's':
                print('FINALIZANDO...')
                sleep(2)
                print(f'{user} OBRIGADO POR JOGAR! ATÉ A PROXIMA.')
                break
            else:
                print('COMEÇANDO NOVO JOGO...')
                sleep(2)

    elif opção == 4:
        print('ENTRANDO NO GAME...')
        sleep(2)
        print('\033[33m-\033[m' * 40)
        print(f'\033[34m{"PAR OU IMPAR":-^40}\033[m')
        print('\033[33m-\033[m' * 40)
        
        ganhos = 0
        user = str(input('Qual é o seu nome? '))
        print(f'Vamos jogar, {user}...')
        sleep(2)
        print('\033[33m-\033[m' * 40)
        
        while True:
            valor_user = int(input('Digite um valor: '))
            valor_comp = randint(1, 50)
            soma = valor_user + valor_comp

            par_impar = str(input('Escolha PAR ou IMPAR [P/I]: ')).strip().upper()
            print('GERANDO RESULTADO...')
            sleep(2)
            print('\033[33m-\033[m' * 40)

            if soma % 2 == 0 and par_impar == 'P' or soma % 2 == 1 and par_impar == 'I':
                ganhos += 1
                tipo = "PAR" if soma % 2 == 0 else "IMPAR"
                print(f'Você jogou: {valor_user}')
                print(f'A máquina jogou: {valor_comp} \nTotal de {soma} dando um número {tipo}!')
                print('\033[33m-\033[m' * 40)
                print(f'\033[32m{"GANHOU":-^40}\033[m')
                print('\033[33m-\033[m' * 40)
            
            else:
                tipo = "PAR" if soma % 2 == 0 else "IMPAR"
                print(f'\033[31m{"PERDEU":-^40}\033[m')
                print('\033[33m-\033[m' * 40)
                print(f'Você jogou: {valor_user}')
                print(f'A máquina jogou: {valor_comp} \nTotal de {soma} dando um número {tipo}!')
                print('\033[33m-\033[m' * 40)
                print('''AQUI ESTÃO AS OPÇÕES
            \033[32m[ 1 ] CONTINUAR\033[m
            \033[31m[ 2 ] SAIR/RESULTADO\033[m''')
                print('\033[33m-\033[m' * 40)
                op = int(input('DIGITE SUA OPÇÃO: '))
                if op == 1:
                    print('PREPARANDO NOVA JOGADA...')
                    print('\033[33m-\033[m' * 40)
                    sleep(2)
                    continue
                else:
                    print('CALCULANDO RESULTADO...')
                    sleep(2)
                    print(f'{user} venceu um total de {ganhos} vezes!')
                    sleep(3)
                    break


    elif opção == 5:
        print('FINALZANDO...')
        sleep(2)
        break
 