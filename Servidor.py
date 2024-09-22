import pickle
from socket import *
from random import randint

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('O servidor esta pronto esperando mensagens')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()# Início do contato com o cliente.
	with connectionSocket:

		# Cria uma lista para enviar ao cliente
		minha_lista = [["Produto ", "Código", "Preço"], ["Vitrola1: ", "0001", "3000"],
					   ["Vitrola2: ", "0002", "5000"], ["Vitrola3: ", "0003", "8000"],
					   ["Disco de vinil Raul Seixas - Há dez mil anos atrás ", "0004", "800"],
					   ["Disco de vinil Mamonas Assassinas", "0005" , "500"],
					   ["Disco de vinil Cazuza - Ideologia", "0006", "300"]]

		# Serializa a lista
		data = pickle.dumps(minha_lista)

		# Envia a lista serializada ao cliente
		connectionSocket.sendall(data)

		precoProduto = 0 # Recebe o preço do produto escolhido para a comparação na hora de negociar.
		inserirCodigo = True

		while True:
			x = "Insira o código do produto desejado: "
			connectionSocket.send(x.encode())

			y = connectionSocket.recv(1024).decode()
			print(f"Código recebido: {y}")

			produtoEncontrado = False # Indica se produto foi ou não encontrado na lista de produtos.
			for produto in minha_lista:
				if produto[1] == y:  # Verifica se o código do produto corresponde ao recebido
					produtoEncontrado = True
					precoProduto = int(produto[2])
					print("Válido.")
					z = f"Produto encontrado: {produto[0]} - Preço: {produto[2]}" # Envia a confirmação de que encontrou o produto na lista.
					connectionSocket.send(z.encode())
					break

			if not produtoEncontrado:
				print("Inválido")
				z = "Produto não encontrado! Tente novamente." # Alerta o usuário de que o código do produto não foi encontrado.
				connectionSocket.send(z.encode())
			else:
				break # Encerra o loop, seguindo para a negociação.

		exeLoop = int(sentence) # Variável que executa o loop das interações, com o limite preestabelecido
		while exeLoop != 0:
			exeLoop -= 1
			x = "Faça uma oferta pelo produto: " # Solicita uma oferta pelo produto.
			connectionSocket.send(x.encode())
			y = connectionSocket.recv(1024).decode()
			print(f"Oferta recebida: {y}")

			random = randint(2, 5) # Sorteio de um número de 2 a 5.
			contraOferta = precoProduto - (random / 100 * precoProduto) # Usa o número sorteado na linha anterior para pra gerar uma contra oferta, com 2% a 5% de desconto.

			if float(y) < precoProduto * 0.7: # Oferta abaixo de 70% do valor original do produto, envia a contra oferta.
				if exeLoop != 0:
					print("Oferta recusada. Enviando contraproposta.")
				else:
					print("Limite de ofertas excedido.")
				z = f"Sua oferta está muito abaixo do preço. Contra-oferta: {str(contraOferta)}."
				connectionSocket.send(z.encode())
			else:
				print("Oferta aceita.")
				z = "Ok! Compra confirmada." # Oferta acima de 70% do valor original do produto, envia a confirmação de compra.
				connectionSocket.send(z.encode())
				break  # Sai do loop de oferta ao confirmar a compra

		# Avisa que a compra não será concluída quando o usuário excede o limite de ofertas.
		if exeLoop == 0:
			x = "Você atingiu o limite de tentativas. Não será possível concluir a compra. Conexão encorrada."
			connectionSocket.send(x.encode())

		print("Conexão encerrada.")
		connectionSocket.close()# Encerramento da conexão












