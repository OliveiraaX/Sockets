import socket
import sys

if len(sys.argv) != 3:
    print("Uso correto: python3 script.py <IP> <Porta>")
    sys.exit(1)

ip_servidor = sys.argv[1]
porta_servidor = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((ip_servidor, porta_servidor))

    while True:
        msg = input("Mensagem: ") + "\n"
        client.send(msg.encode())
        data = client.recv(1024)
        print(f"Servidor: {data.decode()}")

        if data.decode() == "sair\n" or msg == "sair\n":
            break

    client.close()

except Exception as error:
    print("Erro de conexão")
    print(error)
    client.close()
