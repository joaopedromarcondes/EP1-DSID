from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
import grpc
from concurrent import futures
from random import randint
from google.protobuf.empty_pb2 import Empty 

class MensagemServicer(mensagens_pb2_grpc.MensagemServicer):
    
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
    
    def FuncaoVariosLong(self, request, context):
        print("Recebendo Varios Long")
        return mensagens_pb2.MensagemVariosLong(
            valores=[randint(0, 2**63),]
        )
    
    def FuncaoString(self, request, context):
        print("Recebendo String")
        return mensagens_pb2.MensagemString(
            valor="Mensagem String"
        )
    
    def FuncaoComplexa(self, request, context):
        print("Recebendo Mensagem Complexa")
        return mensagens_pb2.MensagemComplexa(
            id=3,
            nome="Mensagem Complexa",
            ativo=True,
            salario=1000.0,
            estadoCivil="Casado",
            filhos=["Filho 1", "Filho 2"],
            cargo="Desenvolvedor",
            idade=30
        )
    

   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensagens_pb2_grpc.add_MensagemServicer_to_server(MensagemServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Começando Servidor....")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()