# GERADOR DE SMS CRIADO POR Leonardo Henrique

from twilio.rest import Client
from time import sleep


print('\033[36m-=\033[m' * 20)
print(f'\033[35m{"SMS / CHAMADAS":^40}\033[m')
print('\033[36m-=\033[m' * 20)

print(f'{"OPÇÕES":^40}')
print('\033[33m-\033[m' * 40)
print('''            \033[32m[ 1 ] CHAMADAS\033[m
            \033[32m[ 2 ] SMS\033[m''')
print('\033[33m-\033[m' * 40)

# Credenciais do Twilio (obtidas na sua conta do Twilio)
account_sid = ''
auth_token = ''

# Crie o cliente Twilio
client = Client(account_sid, auth_token)

# Escolha uma das opções SMS / CHAMADAS
opção = int(input('O QUE VOCÊ DESEJA USAR: '))

if opção == 1:
    # Número de destino
    numero_destino = str(input('DIGITE O NÚMERO DE DESTINO: '))

    # Cria uma chamada
    call = client.calls.create(
        numero_destino, # Número de destino
        from_= '', # Número gerado pelo Twilio
        twiml='<Response><Say voice="alice" language="pt-BR">Bem-vindo ao sistema! Obrigado por testar o Twilio.</Say></Response>'
    )
    print(f'LIGAÇÃO INICIADA COM SID: {call.sid}')

elif opção == 2:
    # Número de destino
    numero_destino = str(input('DIGITE O NÚMERO DE DESTINO: '))

    # Mensagem a ser enviada
    mensagem = str(input('DIGITE A MENSAGEM A SER ENVIADA: '))
    
    # Envia o SMS para o número de destino
    try:
        message = client.messages.create(
            body=mensagem, # Corpo da mensagem
            from_= '', # Número gerado pelo Twilio
            to=numero_destino # Número para onde o SMS será enviado
        ) 
        print(f'MENSAGEM ENVIADA: {message.sid}')
    except Exception as e:
        print(f'ERRO AO ENVIAR A MENSAGEM {e}')
