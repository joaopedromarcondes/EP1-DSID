from comunicacao_grpc import mensagens_pb2, mensagens_pb2_grpc
import grpc
from concurrent import futures
from random import randint
from google.protobuf.empty_pb2 import Empty 

class MensagemServicer(mensagens_pb2_grpc.MensagemServicer):
    
    def FuncaoVoid(self, request, context):
        return Empty()  
    
    def FuncaoLong(self, request, context):
        return mensagens_pb2.MensagemLong(valor=request.valor*2)
    
    def FuncaoVariosLong(self, request, context):
        return mensagens_pb2.MensagemVariosLong(
            valores=[sum(request.valores),]
        )
    
    def FuncaoString(self, request, context):
        return mensagens_pb2.MensagemString(
            valor=request.valor.upper()
        )
    
    def FuncaoComplexa(self, request, context):
        return mensagens_pb2.MensagemComplexa(
            id=request.id,
            nome=request.nome.upper(),
            ativo=not request.ativo,
            salario=request.salario * 1.2,
            estadoCivil=request.estadoCivil,
            filhos=request.filhos,
            cargo=request.cargo,
            idade=request.idade + 1
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