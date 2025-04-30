from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
from google.protobuf.empty_pb2 import Empty
import grpc
import time
from random import randint


def client(ip_dest="localhost"):
    print("Começando Cliente....\n")
    res = dict()
    channel = grpc.insecure_channel(f'{ip_dest}:50051')
    stub = mensagens_pb2_grpc.MensagemStub(channel)

    tempos_Long = []
    for i in range(10):
        val = randint(0, 2**50)
        inicio = time.perf_counter()
        stub.FuncaoLong(mensagens_pb2.MensagemLong(valor=val))
        fim = time.perf_counter()
        tempos_Long.append(fim - inicio)
    res["Long"] = tempos_Long
    

    tempos_Void = []
    for i in range(10):
        val = randint(1, 10)
        inicio = time.perf_counter()
        stub.FuncaoVoid(Empty())
        fim = time.perf_counter()
        tempos_Void.append(fim - inicio)
    res["Void"] = tempos_Void


    tempos_VariosLong = []
    for i in range(10):
        val = [randint(0, 2**50) for _ in range(8)]
        inicio = time.perf_counter()
        stub.FuncaoVariosLong(mensagens_pb2.MensagemVariosLong(valores=val))
        fim = time.perf_counter()
        tempos_VariosLong.append(fim - inicio)
    res["VariosLong"] = tempos_VariosLong

    tempos_String = []
    for i in range(10):
        val = "a" * (2 ** i)
        inicio = time.perf_counter()
        stub.FuncaoString(mensagens_pb2.MensagemString(valor=val))
        fim = time.perf_counter()
        tempos_String.append(fim - inicio)
    res["String"] = tempos_String

    tempos_Complexa = []
    for i in range(10):
        val = "a" * (2 ** i)
        inicio = time.perf_counter()
        stub.FuncaoComplexa(mensagens_pb2.MensagemComplexa(id=1,
        nome="João",
        ativo=True,
        salario=5000.0,
        estadoCivil="Casado",
        filhos=["Ana", "Pedro"],
        cargo="Engenheiro",
        idade=30))
        fim = time.perf_counter()
        tempos_Complexa.append(fim - inicio)
    res["Complexa"] = tempos_Complexa

    return res



if __name__ == "__main__":
    client()