# Use a imagem base do Python com Alpine
FROM python:3.9-alpine

# Instale as dependências do sistema necessárias
RUN apk add --no-cache gcc musl-dev libffi-dev

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto
COPY . .

# Comando para rodar o aplicativo
CMD ["python", "main.py"]