import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = "Servidor: Olá, Cliente!"

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem.")
        s.sendto(dados + (mensagem.encode()), end)