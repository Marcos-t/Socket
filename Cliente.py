import threading
import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('192.168.100.61', 1236))
    except:
        return print('\n Não foi possivel conectar\n')

    Professor = input("Digite o nome do Professor: \n")

    print('Conectado')

    threadReceber = threading.Thread(target=ReceberMensagens, args=[client])
    threadEnviar = threading.Thread(target=EnviarFrequencia, args=[client, Professor])

    threadReceber.start()
    threadEnviar.start()


def ReceberMensagens(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print("\n Não foi possivel permanecer conectado no servidor!\n")
            print("Pressione enter para continuar")
            client.close()
            break


def EnviarFrequencia(client, Professor):
    while True:
        try:
            nomeAluno = input('Digite o Nome do Aluno: \n')
            materia = input('Digite a Materia: \n')
            faltas = int(input('Digite a quantidade de faltas: \n'))
            if faltas > 7:
                status = "Acima do limite de Faltas"
            if faltas <= 7:
                status = "Abaixo do Limite de Faltas"
            frequencia = ["Professor: " + Professor, "Aluno: " + nomeAluno, "Materia: " + materia,
                          "Faltas: " + str(faltas), status]
            msg = frequencia
            client.send(f'{msg}'.encode('utf-8'))
        except:
            return


main()
