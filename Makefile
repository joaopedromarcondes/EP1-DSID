build:  
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. comunicacao_grpc/mensagens.proto

clean:
	rm comunicacao_grpc/mensagens_pb2.py comunicacao_grpc/mensagens_pb2_grpc.py

update:
	pip install -r requirements.txt
