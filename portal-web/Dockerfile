FROM python:3.9-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando arquivos de requisitos para o contêiner
COPY requirements.txt ./requirements.txt 

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante da aplicação para o contêiner 
COPY . app/

# Porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "app/web.py", "--server.fileWatcherType=watchdog"]
