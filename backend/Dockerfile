# Usar imagem oficial do Python
FROM python:3.10

# Diretório de trabalho
WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY . .


EXPOSE 8000
# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]