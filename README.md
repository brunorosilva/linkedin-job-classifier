# NLP - Job Classification

This project is an activity of the Specialization in Artificial Intelligence at PECE-Poli, Natural Language Processing course.

The main objective of this project is to create a model using NLP which will be capable of receiving a job description and to predict what title this professional is most likely to be according to LinkedIn.


## Overview
The project was developed in three phases:
1. LinkedIn Data Scraping to create the dataset;
2. Development of a Deep Learning model for multiclass classification;
3. Development of a web app using Streamlit in order to facilitate the interaction with the model.

### 1. Dataset
The dataset used to train the model was build using web scraping with [Selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py), the scraping script is available in the `scraper/scraper.py` file. 

The scraping process was to search for jobs with the titles of Data Scientist, Data Analyst and Data Engineer (a thousand of each), and to gatter the job description as given by the hiring company.

The dataset will not be available in this repo, due to the fact that no scraping authorization was made neither to LinkedIn nor to the individual companies.

### 2. Model
The model was created using [Tensorflow](https://github.com/tensorflow/tensorflow/) and NLP methods learned during the course.

For a hyperparameter tuning process please refer to `tuning-process-report.html`, which is a sample of the entire parameter search. The complete report was over 400MB and will not be uploaded here.

The best model architecture found was:
- 8 hidden layers with 8 neurons each;
- batch_size=64;
- trained for 20 epochs;
- SGD opt.

Best model diagram, 86.85% accuracy in the test set.

![best_model](imgs/nn.png)

Tuning report of the best model

![TR](imgs/tuning.png)

### 3. Webapp Streamlit

To see the model in action with Streamlit, use
```sh
$ git clone https://github.com/brunorosilva/nlp-classificacao-de-vagas.git
$ cd nlp-classificacao-de-vagas
~/nlp-classificacao-de-vagas $ pip install -r requirements.txt
```
and then
```sh
~/nlp-classificacao-de-vagas $ streamlit run dashboard.py
```
In the dashboard you'll be able to choose among simple examples, examples taken from LinkedIn which were not in the traning nor in the test set or even trying a manual input.

The webapp is extremely simple and it works as a POC, just choose among the options and the dashboard will create a bar plot showing the estimated probability among the three possible job titles.

![Dashboard](imgs/dashboard.png)


# NLP - Classificação de Vagas

Este projeto é uma atividade da Especialização em Inteligência Artificial da PECE-Poli, disciplina de Processamento de Linguagem Natural.


O objetivo deste projeto é a criação de um modelo usando NLP capaz de receber uma descrição de vaga e retornar ao usuário qual é a visão do mercado sobre o título que este funcionário mais se adequa.

## Overview

A motivação deste projeto é como um possível auxílio para construção de equipes de dados por funcionários de RH. O usuário coloca como input do modelo a descrição do funcionário que ele está procurando e o modelo retorna qual título este funcionário mais se adequa em uma equipe de dados, classificando a vaga entre Data Scientist, Data Analyst ou Data Engineer.

O projeto foi desenvolvido a partir de três etapas:
1. Data Scraping do Linkedin para a criação do dataset;
2. Criação de um modelo de Deep Learning para classificação multi-classes;
3. Criação de um webapp para a interação mais fluida com o modelo usando Streamlit.

### 1. Dataset
O Dataset foi criado utilizando [Selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py) a partir de um script de scraping disponível no arquivo `scraper/scraper.py` .

O processo consistiu em pesquisar por vagas de Data Scientist, Data Analyst e Data Engineer (mil de cada título, um título por vez), e buscar a descrição de cada vaga conforme fornecido pela empresa contratante.

O Dataset será disponibilizado somente para o avaliador do projeto, uma vez que não foram solicitadas as autorizações do Linkedin para a realização do scraping e tampouco das empresas envolvidas.

### 2. Modelo
O modelo foi criado utilizando [Tensorflow Keras](https://github.com/tensorflow/tensorflow/) e outros métodos abordados durante o curso.

Para o tuning de hiperparâmetros foi desenvolvido um método personalizado de gridsearch com a criação de um relatório interativo para a obtenção de um modelo com a melhor arquitetura encontrada. O arquivo com todos os testes realizados (mais de 400MB) pode ser solicitado caso necessário, mas um exemplo pequeno deste relatório está disponível no arquivo `tuning-process-report.html.`

A melhor arquitetura de modelo encontrada foi com os seguintes hiperparâmetros:
- 8 camadas ocultas, com 8 neurônios cada;
- função de ativação tanh;
- batch_size=64;
- 20 épocas de treinamento;
- função de custo SGD.

Diagrama do modelo escolhido, com exatidão de 86.85% na base de validação.

![image alt ><](imgs/nn.png)

Recorte do relatório de tuning com o modelo vencedor.

![image alt ><](imgs/tuning.png)


### 3. Webapp Streamlit

Para a interação mais fluida com o modelo foi criado um webapp usando [Streamlit](https://streamlit.io/) e para acessá-lo basta instalar as bibliotecas necessárias

com Git
```sh
$ git clone https://github.com/brunorosilva/nlp-classificacao-de-vagas.git
$ cd nlp-classificacao-de-vagas
~/nlp-classificacao-de-vagas $ pip install -r requirements.txt
```
e usar o comando
```sh
~/nlp-classificacao-de-vagas $ streamlit run dashboard.py
```
onde o usuário pode escolher entre exemplos simples, exemplos tirados do Linkedin que não estão na base de treino nem de teste ou um input manual.

O webapp é extremamente simples e serve como prova de conceito, basta escolher entre as opções e o dashboard criará um gráfico de barras mostrando a probabilidade estimada pelo modelo entre os três títulos possíveis.

![image alt ><](imgs/dashboard.png)
