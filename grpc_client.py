from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
from google.protobuf.empty_pb2 import Empty
import grpc
import time
from random import randint

def calcula_desempenho(tempos):
    res = dict()
    soma = 0
    for i in range(10):
        soma += tempos[i]
    res['media'] = soma / 10
    variancia = 0
    for i in range(10):
        variancia += (tempos[i] - (soma / 10)) ** 2

    res['variancia'] = variancia / 10
    res['desvio_padrao'] = variancia ** 0.5
    return res

def print_desempenho(tempos, nome):
    res = calcula_desempenho(tempos)
    print(nome)
    print(f"Média: {res['media']}")
    print(f"Variância: {res['variancia']}")
    print(f"Desvio Padrão: {res['desvio_padrao']}\n")
    return res



def client():
    print("Começando Cliente....\n")
    channel = grpc.insecure_channel('localhost:50051')
    stub = mensagens_pb2_grpc.MensagemStub(channel)

    tempos_Long = []
    for i in range(10):
        val = randint(0, 2**63)
        inicio = time.perf_counter()
        stub.FuncaoLong(mensagens_pb2.MensagemLong(valor=val))
        fim = time.perf_counter()
        tempos_Long.append(fim - inicio)
        print(inicio)
    print_desempenho(tempos_Long, "Função Long")
    

    tempos_Void = []
    for i in range(10):
        val = randint(1, 10)
        inicio = time.perf_counter()
        stub.FuncaoVoid(Empty())
        fim = time.perf_counter()
        tempos_Void.append(fim - inicio)
    print_desempenho(tempos_Void, "Função Void")



if __name__ == "__main__":
    client()