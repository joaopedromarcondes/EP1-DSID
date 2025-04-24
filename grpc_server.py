from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
import grpc
from concurrent import futures
from random import randint
from google.protobuf.empty_pb2 import Empty 

class MensagemServicer(mensagens_pb2_grpc.MensagemServicer):

    def RecebePessoa(self, request, context):
        print(request)
        return mensagens_pb2.MensagemPessoa(nome="andré")
    
    def FuncaoVoid(self, request, context):
        print("Recebendo Void")
        return Empty()  
    
    def FuncaoLong(self, request, context):
        print(request)
        var = 1
        valor = request.valor
        valor *= var
        print(valor)
        return mensagens_pb2.MensagemLong(valor=valor)
   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensagens_pb2_grpc.add_MensagemServicer_to_server(MensagemServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Começando Servidor....")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()