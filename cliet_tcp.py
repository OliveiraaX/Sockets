import socket
import sys

if len(sys.argv) == 3:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(1)

    try:
        porta = int(sys.argv[2])
        mysocket.connect((sys.argv[1], porta))
        pacotes_recebidos = mysocket.recv(1024).decode()
        print(pacotes_recebidos)

    except socket.timeout:
        print("Conexão falhou: tempo limite excedido.")
    except socket.error as e:
        print(f"Ocorreu um erro na conexão: {e}")
    finally:
        mysocket.close()

else:
    print("Falta de argumento, são necessários 2 argumentos (endereço e porta).")
