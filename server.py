from comunicacao_grpc import com_pb2, com_pb2_grpc
import grpc
from concurrent import futures

class MensagemServicer(com_pb2_grpc.MensagemServicer):

    def RecebePessoa(self, request, context):
        print(request)
        return com_pb2.Pessoa(nome="andré")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    com_pb2_grpc.add_MensagemServicer_to_server(MensagemServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Começando Servidor....")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()