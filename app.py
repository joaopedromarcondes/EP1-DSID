from multiprocessing import Process
import grpc_client
import grpc_server
import json_client
import json_server
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import socket

def gerar_graficos(tempos_grpc, titulo):
    plt.figure(figsize=(10, 6))
    tempos_grpc.mean().plot(kind='bar', yerr=tempos_grpc.std(), capsize=4, color='skyblue', alpha=0.8)
    plt.title(f"{titulo} - Gráfico de Barras com Desvio Padrão")
    plt.ylabel("Tempo (ms)")
    plt.xlabel("Operações")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{titulo}_barras.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=tempos_grpc, ci='sd', marker='o', dashes=False)
    plt.title(f"{titulo} - Gráfico de Linhas com Desvio Padrão")
    plt.ylabel("Tempo (ms)")
    plt.xlabel("Operações")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{titulo}_linhas.png")
    plt.show()


def gerar_grafico_comparativo(tempos_grpc, tempos_json):
    comparativo = pd.DataFrame({
        "gRPC": tempos_grpc.mean(),
        "JSON-RPC": tempos_json.mean()
    })

    comparativo.plot(kind='bar', yerr=[tempos_grpc.std(), tempos_json.std()], capsize=4, color=['skyblue', 'lightgreen'], alpha=0.8)
    plt.title("Comparação de Tempos - gRPC vs JSON-RPC")
    plt.ylabel("Tempo Médio (ms)")
    plt.xlabel("Operações")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("comparacao_tempos.png")
    plt.show()




def salvar_analise(tempos_grpc, tempos_json):
    with open("analise.md", "w") as f:
        f.write("Tempos - gRPC\n")
        f.write(tempos_grpc.to_string())
        f.write("\n\n")
        f.write("Análise de Tempos - gRPC\n")
        f.write(tempos_grpc.describe().to_string())
        f.write("\n\n\n")
        f.write("Tempos - JSON-RPC\n")
        f.write(tempos_json.to_string())
        f.write("\n\n")
        f.write("Análise de Tempos - JSON-RPC\n")
        f.write(tempos_json.describe().to_string())
        f.write("\n")


def get_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
    except Exception:
        ip_local = "127.0.0.1"
    finally:
        s.close()
    return ip_local


def app():
    print("---------------------------------\n")
    print("Bem-vindo ao EP1 de Sistemas Distribuídos")
    print("Grupo: João Pedro e Cleben Junior\n")
    print("############################\n")
    print("Escolha a sua opção:")
    print("1 - executar servidor\n2 - executar clientes\n3 - executar ambos localmente\n4 - Sair\n")
    print("---------------------------------\n")
    entrada = input("Digite a opção desejada: ")
    while entrada not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        entrada = input("Digite a opção desejada: ")
    print("---------------------------------\n")

    if entrada == "1":
        print("Iniciando servidores gRPC e JSON-RPC")
        print("Seu ip local é: ", get_ip_local())
        
        grpc_serv = Process(target=grpc_server.serve)
        grpc_serv.start()
        json_server_process = Process(target=json_server.serve)
        json_server_process.start()
        print("Servidores iniciados. Pressione Ctrl+C para parar.")
        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            grpc_serv.terminate()
            json_server_process.terminate()
            print("Servidores parados.")
            return
    elif entrada == "2":
        ip_dest = input("Digite o IP dos servidores (apenas um IP): ")
        print("Iniciando clientes gRPC e JSON-RPC\n")

        tempos_grpc = grpc_client.client()
        tempos_grpc = pd.DataFrame(tempos_grpc)

        tempos_json = json_client.main()
        tempos_json = pd.DataFrame(tempos_json)

        salvar_analise(tempos_grpc, tempos_json)

        gerar_graficos(tempos_grpc, "gRPC")
        gerar_graficos(tempos_json, "JSON-RPC")
        gerar_grafico_comparativo(tempos_grpc, tempos_json)
        print("Análise salva no arquivo 'analise.txt'. Finalizado os clientes.\n")

    elif entrada == "3":
        print("Executando ambos localmente\n")
        grpc_serv = Process(target=grpc_server.serve)
        grpc_serv.start()
        
        sleep(2)
        tempos_grpc = grpc_client.client()
        tempos_grpc = pd.DataFrame(tempos_grpc)

        grpc_serv.terminate()
        print("Finalizado o servidor gRPC\n")

        json_server_process = Process(target=json_server.serve)
        json_server_process.start()
        sleep(2)
        tempos_json = json_client.main()
        tempos_json = pd.DataFrame(tempos_json)

        json_server_process.terminate()
        print("Finalizado a execução local\n")

        salvar_analise(tempos_grpc, tempos_json)

        gerar_graficos(tempos_grpc, "gRPC")
        gerar_graficos(tempos_json, "JSON-RPC")
        gerar_grafico_comparativo(tempos_grpc, tempos_json)
        print("Análise salva no arquivo 'analise.md'.\n")

    elif entrada == "4":
        print("Saindo do programa...")
        return

if __name__ == "__main__":
    app()