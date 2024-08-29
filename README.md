# Sistema de Consultas Hospitalares com Chatbot

Este projeto é uma aplicação de chatbot para um sistema hospitalar, utilizando sockets e arquivos JSON para gerenciar o cadastro de clientes e agendar consultas. A comunicação entre o cliente e o servidor é feita via sockets, e os dados do cliente são armazenados em arquivos JSON locais.

## Visão Geral

O sistema permite que um cliente se registre, agende, consulte o status e cancele consultas. O servidor lida com as solicitações e armazena os dados do cliente em arquivos JSON, enquanto o cliente interage com o servidor para realizar operações.

## Funcionalidades

- **Cadastro**: O cliente pode se cadastrar enviando seu nome.
- **Agendamento de Consultas**: O cliente pode agendar uma consulta fornecendo a data e a hora.
- **Consulta de Status**: O cliente pode verificar o status da consulta agendada.
- **Cancelamento de Consultas**: O cliente pode cancelar uma consulta agendada.

## Requisitos

- Python 3.x
- Biblioteca padrão de socket
- Biblioteca padrão de json
- Sistema operacional compatível com sockets (Linux, macOS, Windows)

## Estrutura do Projeto

- `servidor.py`: Código do servidor que gerencia o cadastro e as consultas.
- `cliente.py`: Código do cliente que interage com o servidor.
- `README.md`: Este arquivo.

## Configuração e Execução

### 1. Configuração do Servidor

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde os arquivos do projeto estão localizados.
3. Execute o servidor com o seguinte comando:

    ```bash
    python servidor.py
    ```

   O servidor começará a escutar conexões na porta 65432.

### 2. Configuração do Cliente

1. Abra outro terminal ou prompt de comando.
2. Navegue até o diretório onde os arquivos do projeto estão localizados.
3. Execute o cliente com o seguinte comando:

    ```bash
    python cliente.py
    ```

4. O cliente solicitará um ID. Se o ID não estiver cadastrado, será solicitado o registro. Após o registro, você poderá usar os seguintes comandos:
   - `agendar`: Para agendar uma consulta.
   - `status`: Para consultar o status da consulta.
   - `cancelar`: Para cancelar a consulta.
   - `sair`: Para encerrar a interação.

## Uso

### Exemplo de Interação

1. **Cliente Inicia:**
    - O cliente solicita um ID.
    - Se o ID não está cadastrado, o servidor informa que o cliente pode se cadastrar.

2. **Cadastro de Cliente:**
    - O cliente digita `cadastrar`.
    - O cliente insere seu nome quando solicitado.
    - O servidor confirma o cadastro e informa que o cliente pode agora agendar, consultar ou cancelar consultas.

3. **Gerenciamento de Consultas:**
    - O cliente pode digitar `agendar`, `status`, ou `cancelar` para gerenciar consultas.
    - O cliente fornece informações adicionais, como data e hora para agendar a consulta.

### Exemplo de Uso no Cliente

```plaintext
Digite seu ID: Marcos
ID não encontrado. Digite "cadastrar" para se registrar:
Digite 'cadastrar' para se registrar: cadastrar
Digite seu nome: Marcos Silva
Cadastro realizado com sucesso! Agora você pode agendar, consultar ou cancelar sua consulta.
Digite um comando ('agendar', 'status', 'cancelar' ou 'sair'): agendar
Digite a nova data e hora (ex: 20 de agosto às 10:00): 25 de agosto às 14:00
Consulta agendada para 25 de agosto às 14:00.
Digite um comando ('agendar', 'status', 'cancelar' ou 'sair'): status
Status da consulta: 25 de agosto às 14:00
Digite um comando ('agendar', 'status', 'cancelar' ou 'sair'): cancelar
Consulta cancelada.
Digite um comando ('agendar', 'status', 'cancelar' ou 'sair'): sair