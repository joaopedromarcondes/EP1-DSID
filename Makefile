build:
	python3 -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  comunicacao_grpc/com.proto

server:
  python3 server.py

client:
  python3 client.py

instalar_bibliotecas:
  pip install -r requirements.txt

atualizar_bibliotecas:
  pip freeze > requirements.txt