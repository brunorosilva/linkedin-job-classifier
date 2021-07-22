package := "nlp-classificacao-de-vagas"

# launch streamlit app
app:
	poetry run streamlit run dashboard.py

# black and isort
lint:  
	black .
	isort .

