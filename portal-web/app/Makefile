banco:
	python ./criar_banco.py  # <-- TAB aqui

api:
	python ./criar_api.py & sleep 5  # <-- TAB aqui

web:
	streamlit run web.py  # <-- TAB aqui

run: banco api web

stop:
	pkill -f "streamlit run web.py"  # <-- TAB aqui
	pkill -f "python criar_api.py"   # <-- TAB aqui