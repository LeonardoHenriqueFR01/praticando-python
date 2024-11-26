from twilio.rest import Client
from time import sleep
import pywhatkit as kit
from datetime import datetime, timedelta

print('\033[36m-=\033[m' * 20)
print(f'\033[35m{"SMS / CHAMADAS / WHATSAPP":^40}\033[m')
print('\033[36m-=\033[m' * 20)

# Credenciais do Twilio (obtidas na sua conta do Twilio)
account_sid = ''
auth_token = ''

# Crie o cliente Twilio
client = Client(account_sid, auth_token)

def enviar_chamada():
    numero_destino = input('DIGITE O NÚMERO DE DESTINO: ')
    print('PROCESSANDO...')
    sleep(2)

    # Cria uma chamada
    call = client.calls.create(
        to=numero_destino,  # Número de destino
        from_='',  # Número gerado pelo Twilio
        twiml='<Response><Say voice="alice" language="pt-BR">Bem-vindo ao sistema! Obrigado por testar o Twilio.</Say></Response>'
    )
    print(f'LIGAÇÃO INICIADA COM SID: {call.sid}')
    sleep(5)

def enviar_sms():
    numero_destino = input('DIGITE O NÚMERO DE DESTINO: ')
    mensagem = input('DIGITE A MENSAGEM A SER ENVIADA: ')
    print('PROCESSANDO...')
    sleep(2)
    
    try:
        # Envia o SMS para o número de destino
        message = client.messages.create(
            body=mensagem,  # Corpo da mensagem
            from_='',  # Número gerado pelo Twilio
            to=numero_destino  # Número para onde o SMS será enviado
        ) 
        print(f'MENSAGEM ENVIADA: {message.sid}')
        sleep(5)
    except Exception as e:
        print(f'ERRO AO ENVIAR A MENSAGEM: {e}')

def enviar_whatsapp():
    try:
        # Lista de números de destino com o código do país (+55)
        numeros_destino = ['']

        # Mensagem promocional a ser enviada
        mensagem = ''

        # Horário atual (adiciona um pequeno atraso para abrir o WhatsApp Web)
        horario_atual = datetime.now() + timedelta(minutes=2)  # Atrasando para garantir tempo suficiente
        hora = horario_atual.hour
        minuto = horario_atual.minute

        # Enviar a mensagem para cada número na lista
        for numero_destino in numeros_destino:
            print(f"Enviando mensagem para {numero_destino} às {hora}:{minuto}...")

            # Envia a mensagem para o número
            kit.sendwhatmsg(
                numero_destino,  # Número de destino
                mensagem,         # Mensagem de texto
                hora,             # Hora para o envio
                minuto            # Minuto para o envio
            )
            print(f"Mensagem enviada automaticamente para {numero_destino}!")

    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")

# Menu de opções
while True:
    print(f'{"OPÇÕES":^40}')
    print('\033[33m-\033[m' * 40)
    print('''                \033[32m[ 1 ] CHAMADAS\033[m
                \033[32m[ 2 ] SMS\033[m
                \033[32m[ 3 ] WHATSAPP\033[m
                \033[31m[ 4 ] SAIR\033[m''')
    print('\033[33m-\033[m' * 40)

    # Escolha uma das opções
    opção = int(input('O QUE VOCÊ DESEJA USAR: '))

    if opção == 4:
        print('FINALIZANDO...')
        sleep(2)
        break

    elif opção == 1:
        enviar_chamada()
    
    elif opção == 2:
        enviar_sms()
    
    elif opção == 3:
        enviar_whatsapp()
    else:
        print("Opção inválida. Tente novamente.")
