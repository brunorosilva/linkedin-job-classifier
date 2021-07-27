import numpy as np
import pandas as pd
import streamlit as st
from examples import long_da, long_de, long_ds
from nlp_helpers import (binarizar, indice_de_palavras, limpar, sem_stops,
                         stemizar, tokenizar, vocab)
from plotly import express as px
from tensorflow.keras.models import load_model

st.title("Modelo de Classificação de Vagas")
descricao_vaga = None

inputs_possiveis = st.radio(
    "Selecione a maneira que você quer dar o input do modelo",
    ["Exemplos toy", "Exemplos reais do Linkedin", "Input customizado"],
)
if inputs_possiveis == "Exemplos toy":
    tipo_de_vaga = st.radio(
        "Exemplos toy são descrições simples de cada função, criadas por mim sem nenhuma descrição de vaga como referência",
        ["", "Data Scientist", "Data Analyst", "Data Engineer"],
        format_func=lambda x: "Selecione uma opção" if x == "" else x,
    )
    if tipo_de_vaga == "Data Scientist":
        descricao_vaga_tmp = "This professional will be responsible for analysis and machine learning models"
        st.markdown("Input no Modelo:\n\n" + descricao_vaga_tmp)
        descricao_vaga = descricao_vaga_tmp
    elif tipo_de_vaga == "Data Analyst":
        descricao_vaga_tmp = "This professional will be responsible for analysis using BI tools and strategic decisions"
        st.markdown("Input no Modelo:\n\n" + descricao_vaga_tmp)
        descricao_vaga = descricao_vaga_tmp
    elif tipo_de_vaga == "Data Engineer":
        descricao_vaga_tmp = "This professional will be responsible for creating data pipelines and cloud performance"
        st.markdown("Input no Modelo:\n\n" + descricao_vaga_tmp)
        descricao_vaga = descricao_vaga_tmp

# exemplos_btn_linkedin = st.checkbox("Clique aqui se quiser ver alguns exemplos tirados do Linkedin")
if inputs_possiveis == "Exemplos reais do Linkedin":
    tipo_de_vaga = st.radio(
        "Estes foram exemplos que eu tirei diretamente do meu Linkedin e não estão nas bases usadas no modelo e nem tem o título da função na descrição da vaga",
        [
            "",
            "Data Scientist @ Volvo",
            "Data Analyst @ Dentsu International",
            "Data Engineer @ Amify",
        ],
        format_func=lambda x: "Selecione uma opção" if x == "" else x,
    )
    if tipo_de_vaga == "Data Scientist @ Volvo":
        descricao_vaga_tmp = long_ds
        st.markdown("Input no Modelo:\n\n" + descricao_vaga_tmp)
        descricao_vaga = descricao_vaga_tmp
    elif tipo_de_vaga == "Data Analyst @ Dentsu International":
        descricao_vaga_tmp = long_da
        st.markdown("Input no Modelo:\n\n" + descricao_vaga_tmp)
        descricao_vaga = descricao_vaga_tmp
    elif tipo_de_vaga == "Data Engineer @ Amify":
        descricao_vaga_tmp = long_de
        st.markdown("Input no Modelo:\n\n" + descricao_vaga_tmp)
        descricao_vaga = descricao_vaga_tmp

# exemplos_btn_custom = st.checkbox("Clique aqui se quiser colocar um input personalizado (em inglês)")

if inputs_possiveis == "Input customizado":
    descricao_vaga = st.text_area(
        "Coloque abaixo a descrição de uma vaga de Data Scientist, Data Analyst ou Data Engineer. \n\nRecomendo copiar a descrição de uma vaga vinda do linkedin.",
        height=500,
    )

model = load_model("streamlit_app/nlp_model")

if descricao_vaga:

    descricao_vaga_token = stemizar(sem_stops(limpar(tokenizar(descricao_vaga))))

    vetores_msg = np.array([indice_de_palavras[p] for p in descricao_vaga_token])

    vetores_msg_bin = binarizar([vetores_msg])

    predicao = model.predict(
        np.array(
            [
                vetores_msg_bin,
            ]
        )
    )
    predicao_dict = {0: "Data Scientist", 1: "Data Analyst", 2: "Data Engineer"}
    # if not exemplos_btn_linkedin and not exemplos_btn_simples:
    #     prefix = "Este profissional deve ser um "
    #     st.markdown(prefix + predicao_dict[np.argmax(predicao, axis=-1)[0][0]])

    df = pd.DataFrame(
        {
            "Profissão": ["Data Scientist", "Data Analyst", "Data Engineer"],
            "Probabilidade": [round(i * 100, 2) for i in predicao[0][0]],
        }
    )

    fig = px.bar(
        df,
        "Profissão",
        "Probabilidade",
        text="Probabilidade",
        range_color=[0, 100],
        color="Probabilidade",
        color_continuous_scale="blues",
    )
    fig.update_layout(yaxis_range=[0, 100], hovermode="x", height=500)
    fig.update(layout_coloraxis_showscale=False)
    fig.update_traces(textposition="outside")

    st.plotly_chart(fig)
