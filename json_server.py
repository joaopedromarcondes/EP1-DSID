# server.py
import jsonrpcserver 

@jsonrpcserver.method
def soma(a, b):
    return jsonrpcserver.Success(a + b)

def serve():
    print("Iniciando servidor JSON-RPC...")
    jsonrpcserver.serve("localhost", 5000)

if __name__ == "__main__":
    serve()
