from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
from google.protobuf.empty_pb2 import Empty
import grpc

def client():
    print("Começando Cliente....")
    channel = grpc.insecure_channel('localhost:50051')
    stub = mensagens_pb2_grpc.MensagemStub(channel)
    nome = "Andre"

    print(stub.FuncaoLong(mensagens_pb2.MensagemLong(valor=10)))

    response = stub.FuncaoVoid(Empty())
    print("Função void chamada com sucesso")


if __name__ == "__main__":
    client()