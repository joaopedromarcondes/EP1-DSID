# EP1 - DSID

Este é o README para a aplicação desenvolvida como parte do EP1 da disciplina DSID. Abaixo estão as instruções detalhadas para configurar e usar a aplicação.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:
- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads) (opcional, para clonar o repositório)

## Instalação

1. Clone o repositório ou baixe os arquivos:
    ```bash
    git clone https://github.com/joaopedromarcondes/EP1-DSID.git
    cd EP1
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação:
    ```bash
    python app.py
    ```

2. Siga as instruções exibidas no terminal.

## Estrutura do Projeto

- `app.py`: Arquivo principal para execução da aplicação.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Documentação do projeto.
- `grpc_server.py`, `grpc_client.py`, `json_server.py`, `json_client.py`: Arquivos de execução dos clientes e servidores.
- `resultados/`: Pasta com os resultados de cada teste aplicado.
- `Makefile`: Arquivo com a execução de comandos recorrentes durante o desenvolvimento.


## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: [joaopopm@gmail.com](mailto:joaopopm@gmail.com) ou [clebenjuniorcgarcia@hotmail.com](mailto:clebenjuniorcgarcia@hotmail.com).
