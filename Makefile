package := "nlp-classificacao-de-vagas"

# launch streamlit app
app:
	poetry run streamlit run streamlit_app/app.py

# black and isort
lint:  
	black .
	isort .

