import os


def processar_resposta(resposta, nome): 
    if resposta == '1':
        print(f'{os.linesep}{nome} , o preço referente ao seu pedido é R$ 32,00, o mesmo será entregue em até 40 minutos. A pizzaria Veteranos agradece pela sua preferência!{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} , o preço referente ao seu pedido é R$ 35,00, o mesmo será entregue em até 40 minutos. A pizzaria Veteranos agradece pela sua preferência!{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} , o preço referente ao seu pedido é R$ 30,00, o mesmo será entregue em até 40 minutos. A pizzaria Veteranos agradece pela sua preferência!{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} , o preço referente ao seu pedido é R$ 29,00, o mesmo será entregue em até 40 minutos. A pizzaria Veteranos agradece pela sua preferência!{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome} , o preço referente ao seu pedido é R$ 30,00, o mesmo será entregue em até 40 minutos. A pizzaria Veteranos agradece pela sua preferência!{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a Pizzaria Veteranos')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    # pedir o telefone
    telefone = input('Digite o seu telefone: ')
    # pedir o endereço
    endereco = input('Digite o seu endereço (Rua, Número e Complemento): ')
    while True: 
        # Oferer o menu de opções
        resposta = input (
            f'O que gostaria de pedir hoje? (Digite apenas 1, 2, 3, 4 ou 5){os.linesep}[1] - A MODA DA CASA{os.linesep}[2] - PALMITO{os.linesep}[3] - FRANGO {os.linesep}[4] - BANANA{os.linesep}[5] - PRESTIGIO {os.linesep} ') 
        # Processar a resposta enviada
        
        return processar_resposta(resposta, nome)
 
if __name__ == '__main__':   
    start()

  