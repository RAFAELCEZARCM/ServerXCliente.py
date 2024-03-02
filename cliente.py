import socket 
import time

# Configurações do cliente
host = '127.0.0.1'
port = 12345

# Criação do socket do cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adiciona um loop para tentar se conectar até que a conexão seja estabelecida
while True:
    try:
        cliente_socket.connect((host, port))
        break  # Se a conexão for bem-sucedida, sai do loop
    except ConnectionRefusedError:
        print("Tentando se reconectar...")
        time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente

# Recebe a mensagem do servidor
data = cliente_socket.recv(1024)
print(f"Mensagem do servidor: {data.decode()}")

# Envia dados para o servidor
message_to_send = "Olá, servidor! Sou o cliente."
cliente_socket.send(message_to_send.encode())

# Fecha a conexão
cliente_socket.close()
