# Imagem oficial do Python 2.7
FROM python:2.7-slim

# Diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . /app

# Comando para rodar a aplicação
CMD ["python", "codigo_legado.py"]
