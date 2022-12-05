import threading
import socket

clients = []
frequencia = []


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(("0.0.0.0", 1236))
        server.listen()
    except:
        return print('\n Não foi possivel iniciar um servidor!\n')
 
    while True:
        client, addr = server.accept()
        clients.append(client)

        threadReceberFrequencia = threading.Thread(target=ReceberFrequencia, args=[client])
        threadReceberFrequencia.start()


def ReceberFrequencia(client):
    while True:
        try:
            msg = client.recv(2048)
            frequencia.append(eval(msg.decode('utf-8')))
            print(frequencia)
        except:
            deleteCliente(client)
            break

def deleteCliente(client):
    clients.remove(client)


main()
