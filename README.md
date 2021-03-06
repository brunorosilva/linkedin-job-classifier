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


# NLP - Classifica????o de Vagas

Este projeto ?? uma atividade da Especializa????o em Intelig??ncia Artificial da PECE-Poli, disciplina de Processamento de Linguagem Natural.


O objetivo deste projeto ?? a cria????o de um modelo usando NLP capaz de receber uma descri????o de vaga e retornar ao usu??rio qual ?? a vis??o do mercado sobre o t??tulo que este funcion??rio mais se adequa.

## Overview

A motiva????o deste projeto ?? como um poss??vel aux??lio para constru????o de equipes de dados por funcion??rios de RH. O usu??rio coloca como input do modelo a descri????o do funcion??rio que ele est?? procurando e o modelo retorna qual t??tulo este funcion??rio mais se adequa em uma equipe de dados, classificando a vaga entre Data Scientist, Data Analyst ou Data Engineer.

O projeto foi desenvolvido a partir de tr??s etapas:
1. Data Scraping do Linkedin para a cria????o do dataset;
2. Cria????o de um modelo de Deep Learning para classifica????o multi-classes;
3. Cria????o de um webapp para a intera????o mais fluida com o modelo usando Streamlit.

### 1. Dataset
O Dataset foi criado utilizando [Selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py) a partir de um script de scraping dispon??vel no arquivo `scraper/scraper.py` .

O processo consistiu em pesquisar por vagas de Data Scientist, Data Analyst e Data Engineer (mil de cada t??tulo, um t??tulo por vez), e buscar a descri????o de cada vaga conforme fornecido pela empresa contratante.

O Dataset ser?? disponibilizado somente para o avaliador do projeto, uma vez que n??o foram solicitadas as autoriza????es do Linkedin para a realiza????o do scraping e tampouco das empresas envolvidas.

### 2. Modelo
O modelo foi criado utilizando [Tensorflow Keras](https://github.com/tensorflow/tensorflow/) e outros m??todos abordados durante o curso.

Para o tuning de hiperpar??metros foi desenvolvido um m??todo personalizado de gridsearch com a cria????o de um relat??rio interativo para a obten????o de um modelo com a melhor arquitetura encontrada. O arquivo com todos os testes realizados (mais de 400MB) pode ser solicitado caso necess??rio, mas um exemplo pequeno deste relat??rio est?? dispon??vel no arquivo `tuning-process-report.html.`

A melhor arquitetura de modelo encontrada foi com os seguintes hiperpar??metros:
- 8 camadas ocultas, com 8 neur??nios cada;
- fun????o de ativa????o tanh;
- batch_size=64;
- 20 ??pocas de treinamento;
- fun????o de custo SGD.

Diagrama do modelo escolhido, com exatid??o de 86.85% na base de valida????o.

![image alt ><](imgs/nn.png)

Recorte do relat??rio de tuning com o modelo vencedor.

![image alt ><](imgs/tuning.png)


### 3. Webapp Streamlit

Para a intera????o mais fluida com o modelo foi criado um webapp usando [Streamlit](https://streamlit.io/) e para acess??-lo basta instalar as bibliotecas necess??rias

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
onde o usu??rio pode escolher entre exemplos simples, exemplos tirados do Linkedin que n??o est??o na base de treino nem de teste ou um input manual.

O webapp ?? extremamente simples e serve como prova de conceito, basta escolher entre as op????es e o dashboard criar?? um gr??fico de barras mostrando a probabilidade estimada pelo modelo entre os tr??s t??tulos poss??veis.

![image alt ><](imgs/dashboard.png)
