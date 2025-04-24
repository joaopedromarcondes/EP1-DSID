# json-client.py
import requests
import json

def call_json_rpc(method, params, id):
    url = "http://localhost:5001"
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": id
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

def main():
    print("Chamada para FuncaoVoid:")
    response = call_json_rpc("FuncaoVoid", {}, 1)
    print(response)

    print("\nChamada para FuncaoLong:")
    response = call_json_rpc("FuncaoLong", {"valor": 10}, 2)
    print(response)

    print("\nChamada para FuncaoVariosLong:")
    response = call_json_rpc("FuncaoVariosLong", {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}, 3)
    print(response)

    print("\nChamada para FuncaoString:")
    for i in range(0, 11): 
        tamanho = 2 ** i
        string_teste = "a" * tamanho 
        response = call_json_rpc("FuncaoString", {"valor": string_teste}, 4)
        print(response)

    print("\nChamada para FuncaoComplexa:")
    response = call_json_rpc("FuncaoComplexa", {
        "id": 1,
        "nome": "João",
        "ativo": True,
        "salario": 5000.0,
        "estadoCivil": "Casado",
        "filhos": ["Ana", "Pedro"],
        "cargo": "Engenheiro",
        "idade": 30
    }, 5)
    print(response)

if __name__ == "__main__":
    main()