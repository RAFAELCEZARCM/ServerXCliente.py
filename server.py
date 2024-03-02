#biblioteca socket
import socket 

#Configurando o servidor para local
host = '127.0.0.1'
port = 12345

#Socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(5)

print(f"Servidor escutando em {host}:{port}")

#Aceita a conexão do cliente
cliente_socket, addr = server_socket.accept()
print(f"Conexão recebida de {addr}")

#Define a mensagem a ser enviada pro cliente
message_to_send = "Olá cliente... testando comunicação!"
cliente_socket.send(message_to_send.encode())

#Recebe dados do cliente 
data = cliente_socket.recv(1024)
print(f"Dados recebidos do cliente: {data.decode()}")

#Fechando as conexões
cliente_socket.close()
server_socket.close()




