from multiprocessing import Process
import grpc_client
import grpc_server
import json_client
import json_server
from time import sleep




def app():
    grpc_serv = Process(target=grpc_server.serve)
    grpc_serv.start()
    
    sleep(2)
    grpc_client.client()

    grpc_serv.terminate()

    print("Finalizado o servidor gRPC\n")

    json_server_process = Process(target=json_server.serve)
    json_server_process.start()
    sleep(2)
    json_client.main()
    json_server_process.terminate()





if __name__ == "__main__":
    app()