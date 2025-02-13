banco:
	python ./criar_banco.py

api:
	python ./criar_api.py & sleep 5

web:
	streamlit run web.py

run: banco api web

stop:
	pkill -f "streamlit run web.py"
	pkill -f "python criar_api.py"