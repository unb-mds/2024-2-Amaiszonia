banco:
	python ./criar_banco.py

# Rodar o script da API
api:
	python ./criar_api.py & sleep 2

# Rodar o Streamlit
web:
	streamlit run web.py

# Rodar tudo em sequência
run: banco api web