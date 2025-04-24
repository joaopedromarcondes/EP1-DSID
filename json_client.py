# json-client.py
import requests
import json
import time

# retorna o tempo executado
def call_json_rpc(method, params, id):
    url = "http://localhost:5001"
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": id
    }
    data = json.dumps(payload)
    inicio = time.perf_counter()
    requests.post(url, data=data, headers=headers)
    fim = time.perf_counter()
    return fim - inicio

def main():
    res = dict()
    
    tempo_Void = []
    for _ in range(10):
        tempo_Void.append(call_json_rpc("FuncaoVoid", {}, 1))
    res["Void"] = tempo_Void

    tempo_Long = []
    for _ in range(10):
        tempo_Long.append(call_json_rpc("FuncaoLong", {"valor": 10}, 2))
    res["Long"] = tempo_Long

    tempo_VariosLong = []
    for _ in range(10):
        tempo_VariosLong.append(call_json_rpc("FuncaoVariosLong", {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}, 3))
    res["VariosLong"] = tempo_VariosLong

    tempo_String = []
    for i in range(0, 10): 
        tamanho = 2 ** i
        string_teste = "a" * tamanho 
        tempo_String.append(call_json_rpc("FuncaoString", {"valor": string_teste}, 4))
    res["String"] = tempo_String

    tempo_Complexa = []
    for i in range(0, 10): 
        tamanho = 2 ** i
        string_teste = "a" * tamanho 
        tempo_Complexa.append(call_json_rpc("FuncaoComplexa", {
            "id": 1,
            "nome": "Joao",
            "ativo": True,
            "salario": 5000.0,
            "estadoCivil": "Casado",
            "filhos": ["Ana", "Pedro"],
            "cargo": "Engenheiro",
            "idade": 30
        }, 5))
    res["Complexa"] = tempo_Complexa
    

    return res

if __name__ == "__main__":
    main()