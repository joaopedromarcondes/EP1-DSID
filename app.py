from multiprocessing import Process
import grpc_client
import grpc_server
import json_client
import json_server
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def app():
    grpc_serv = Process(target=grpc_server.serve)
    grpc_serv.start()
    
    sleep(2)
    tempos_grpc = grpc_client.client()
    tempos_grpc = pd.DataFrame(tempos_grpc)
    print(tempos_grpc)
    print(tempos_grpc.describe())

    gerar_graficos(tempos_grpc, "gRPC")

    grpc_serv.terminate()

    print("Finalizado o servidor gRPC\n")

    json_server_process = Process(target=json_server.serve)
    json_server_process.start()
    sleep(2)
    tempos_json = json_client.main()
    tempos_json = pd.DataFrame(tempos_json)
    print(tempos_json)
    print(tempos_json.describe())

    gerar_graficos(tempos_json, "JSON-RPC")

    json_server_process.terminate()


if __name__ == "__main__":
    app()