import jsonrpcserver 

@jsonrpcserver.method
def soma(a, b):
    return jsonrpcserver.Success(a + b)

@jsonrpcserver.method
def FuncaoVoid():
    return jsonrpcserver.Success(None)

@jsonrpcserver.method
def FuncaoLong(valor):
    return jsonrpcserver.Success(valor * 2)

@jsonrpcserver.method
def FuncaoVariosLong(a, b, c, d, e, f, g, h):
    resultado = a + b + c + d + e + f + g + h
    return jsonrpcserver.Success(resultado)

@jsonrpcserver.method
def FuncaoString(valor):
    return jsonrpcserver.Success(valor.upper())

@jsonrpcserver.method
def FuncaoComplexa(id, nome, ativo, salario, estadoCivil, filhos, cargo, idade):
    resultado = {
        "id": id,
        "nome": nome.upper(),
        "ativo": not ativo,
        "salario": salario * 1.2,
        "estadoCivil": estadoCivil,
        "filhos": filhos,
        "cargo": cargo,
        "idade": idade + 1
    }
    return jsonrpcserver.Success(resultado)

def serve():
    print("Iniciando servidor JSON-RPC...")
    jsonrpcserver.serve("0.0.0.0", 5001)

if __name__ == "__main__":
    serve()
