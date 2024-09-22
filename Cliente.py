import pickle
from socket import *
from random import randint
serverName = '192.168.100.24'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
random = randint(3, 6) # Sorteio de um número entre 3 e 6, que será o limite de interações com o servidor
sentence = str(random)
clientSocket.send(sentence.encode()) #inicia a interação com o servidor já definindo o limite de interações na negociação
data = clientSocket.recv(1024)

# Recebe a lista de produtos do servidor e trasnforma em uma string pra immprimir na tela em formato de tabela
if data:
    lista_recebida = pickle.loads(data)
    for i in lista_recebida:
        stringLista = " - ".join(i)
        print(stringLista)

# O usuário envia o código do produto desejado e recebe a resposta de servidor, se o código foi encontrado ou se será necessário fazer uma nova tentativa.
while True:
    x = clientSocket.recv(1024).decode()

    y = input(x)
    clientSocket.send(y.encode())

    z = clientSocket.recv(1024).decode()
    print(z)

    if z.__contains__("Produto encontrado:"):
        break

exeLoop = int(sentence) # Variável que executa o loop das interações, com o limite preestabelecido
while exeLoop != 0:
    exeLoop -= 1
    x = clientSocket.recv(1024).decode()
    y = input(x)
    clientSocket.send(y.encode())

    z = clientSocket.recv(1024).decode()
    print(z)

    if "Ok! Compra confirmada." in z:
        print("Compra realizada com sucesso!")
        break  # Sai do loop quando a compra é confirmada

# Quando o usuário excede o limite de ofertas, o servidor avisa que não será possível concluir a compra.
if exeLoop == 0:
    x = clientSocket.recv(1024).decode()
    print(x)

clientSocket.close() # Encerramento da conexão











