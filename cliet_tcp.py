{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang22 import socket\par
import sys\par
\par
if len(sys.argv) == 3:\par
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\par
    mysocket.settimeout(1)\par
\par
    try:\par
        porta = int(sys.argv[2])\par
        mysocket.connect((sys.argv[1], porta))\par
        mysocket.send(b"Estou conectado?\\n")\par
        pacotes_recebidos = mysocket.recv(1024).decode()\par
        print(pacotes_recebidos)\par
\par
    except socket.timeout:\par
        print("Conex\'e3o falhou: tempo limite excedido.")\par
    except socket.error as e:\par
        print(f"Ocorreu um erro na conex\'e3o: \{e\}")\par
    finally:\par
        mysocket.close()\par
\par
else:\par
    print("Falta de argumento, s\'e3o necess\'e1rios 2 argumentos (endere\'e7o e porta).")\par
}
 