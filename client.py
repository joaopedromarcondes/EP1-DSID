from comunicacao_grpc import com_pb2_grpc, com_pb2
import grpc

def client():
    print("Começando Cliente....")
    channel = grpc.insecure_channel('grpc-server:50051')
    stub = com_pb2_grpc.MensagemStub(channel)
    nome = "Andre"
    pessoa = com_pb2.Pessoa(nome=nome)
    feature = stub.RecebePessoa(pessoa)
    print(feature)


if __name__ == "__main__":
    client()