FROM python:slim

WORKDIR /app

# Instala as dependências
RUN pip install --no-cache-dir grpcio grpcio-tools

# Compila os arquivos .proto
CMD ["python"]

