#ProjetoServidorXClientePython

##Descrição:
Este projeto em Python apresenta um servidor e cliente que realizam uma comunicação bidirecional usando sockets. 
O servidor aceita conexões, envia uma mensagem inicial ao cliente e espera os dados do cliente. O cliente se conecta ao servidor, recebe a mensagem inicial e envia uma resposta ao servidor.

##Funcionalidades:
#Servidor:
Aceita conexões de clientes.
Envia mensagem inicial para o cliente.
Aguarda dados do cliente e imprime na tela.

#Cliente:
Conecta-se ao servidor.
Recebe mensagem inicial do servidor.
Envia mensagem para o servidor.

#Uso:
Execute o servidor antes do cliente.
O servidor escutará por conexões na porta especificada.
O cliente se conectará ao servidor, trocará mensagens e fechará a conexão.

#Requisitos:
- Python 3.x

#Notas:
- Ajuste o código conforme necessário para suas configurações de rede e requisitos específicos.
- O código do cliente inclui uma lógica de reconexão simples para lidar com falhas de conexão.

