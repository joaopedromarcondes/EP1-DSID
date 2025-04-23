from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
import grpc

def client():
    print("Começando Cliente....")
    channel = grpc.insecure_channel('localhost:50051')
    stub = mensagens_pb2_grpc.MensagemStub(channel)
    nome = "Andre"
    pessoa = mensagens_pb2.Pessoa(nome=nome)
    feature = stub.RecebePessoa(pessoa)
    print(feature)


if __name__ == "__main__":
    client()