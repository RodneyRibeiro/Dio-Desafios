"""Gerar uma conexão TCP utilizando Python
"""
import socket
import sys


def main():
    """Gerar uma conexão TCP utilizando Python
"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket Criado com Sucesso")

    host_alvo = input("Digite o IP: ")
    porta_alvo = input("Digite a porta: ")

    try:
        s.connect((host_alvo,int(porta_alvo)))
        print("TCP conectado com Sucesso no IP: " + host_alvo + " e na porta: " + porta_alvo)
        s.shutdown(2)
    except socket.error as e:
        print("Conexão falhou no IP: " + host_alvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()

# EOF