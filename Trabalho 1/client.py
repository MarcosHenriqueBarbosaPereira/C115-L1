import socket

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 65432))

    cliente_id = input("Digite seu ID: ")
    cliente.send(cliente_id.encode())

    mensagem = cliente.recv(1024).decode()
    print(mensagem)

    if mensagem.startswith("ID nao encontrado"):
        cadastro = input("Digite 'cadastrar' para se registrar: ").strip()
        if cadastro == 'cadastrar':
            nome = input("Digite seu nome: ")
            dados_cadastro = f"cadastrar:{nome}"
            cliente.send(dados_cadastro.encode())
            resposta = cliente.recv(1024).decode()
            print(resposta)
            resposta = cliente.recv(1024).decode()
            print(resposta)

    while True:
        comando = input("Digite um comando ('agendar', 'status', 'cancelar' ou 'sair'): ")
        if comando == 'sair':
            break
        cliente.send(comando.encode())
        resposta = cliente.recv(1024).decode()
        print(resposta)
    
    cliente.close()

if __name__ == "__main__":
    main()
