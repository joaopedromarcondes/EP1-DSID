# server.py
from jsonrpcserver import method, serve, Success

@method
def soma(a, b):
    return Success(a + b)

if __name__ == "__main__":
    print("Iniciando servidor JSON-RPC...")
    serve("localhost", 5000)
