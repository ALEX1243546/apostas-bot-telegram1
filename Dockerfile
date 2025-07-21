# Usa Python 3.11 como base
FROM python:3.11-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os ficheiros para o container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Define a variável de ambiente TELEGRAM_TOKEN, opcional (podes usar via Render dashboard também)
# ENV TELEGRAM_TOKEN=teu_token

# Comando para iniciar o bot
CMD ["python", "bot_telegram.py"]
