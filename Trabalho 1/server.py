import socket
import json
import os

# Função para salvar dados em um arquivo JSON
def salvar_dados_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f)

# Função para carregar dados de um arquivo JSON
def ler_dados_json(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    return {}

def processar_requisicao(mensagem, cliente_id):
    dados_cliente = ler_dados_json(f'{cliente_id}.json')
    
    if mensagem == "agendar":
        nova_data = input("Digite a nova data e hora (ex: 20 de agosto às 10:00): ")
        dados_cliente['consulta'] = nova_data
        salvar_dados_json(f'{cliente_id}.json', dados_cliente)
        return f"Consulta agendada para {nova_data}."
    elif mensagem == "status":
        consulta = dados_cliente.get('consulta', 'Nenhuma consulta agendada.')
        return f"Status da consulta: {consulta}"
    elif mensagem == "cancelar":
        dados_cliente.pop('consulta', None)
        salvar_dados_json(f'{cliente_id}.json', dados_cliente)
        return "Consulta cancelada."
    else:
        return "Comando não reconhecido."

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 65432))
    servidor.listen()

    print("Aguardando conexão...")
    conexao, endereco = servidor.accept()
    with conexao:
        print(f"Conectado a {endereco}")
        cliente_id = conexao.recv(1024).decode()

        if os.path.exists(f'{cliente_id}.json'):
            conexao.send(b'Bem-vindo ao sistema hospitalar! Digite "agendar", "status" ou "cancelar" para gerenciar suas consultas.')
        else:
            conexao.send(b'ID nao encontrado. Digite "cadastrar" para se registrar.')
            while True:
                mensagem = conexao.recv(1024).decode()
                if mensagem.startswith("cadastrar:"):
                    nome = mensagem[len("cadastrar:"):].strip()
                    dados_cliente = {
                        'nome': nome,
                        'consulta': None
                    }
                    salvar_dados_json(f'{cliente_id}.json', dados_cliente)
                    resposta = "Cadastro realizado com sucesso! Agora você pode agendar, consultar ou cancelar sua consulta."
                    conexao.send(resposta.encode())
                    break
                else:
                    resposta = "Por favor, envie o comando de cadastro no formato 'cadastrar:nome'."
                    conexao.send(resposta.encode())
            # Depois do cadastro, continua com o processamento normal
            conexao.send(b'Bem-vindo ao sistema hospitalar! Digite "agendar", "status" ou "cancelar" para gerenciar suas consultas.')

        while True:
            mensagem = conexao.recv(1024).decode()
            if not mensagem:
                break
            if os.path.exists(f'{cliente_id}.json'):
                resposta = processar_requisicao(mensagem, cliente_id)
            else:
                resposta = "Por favor, registre-se primeiro."
            conexao.send(resposta.encode())

if __name__ == "__main__":
    main()
