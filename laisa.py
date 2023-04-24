# -*- coding: utf-8 -*-
"""laisa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z8kkj557e8hxFo3zYONHgf8dSgIs8rbF
"""

import pandas as pd
import plotly.express as px
import streamlit as st


#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual a sua unidade federativa?', estados)


#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual a sua pesquisa?', colunas)


#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})
(color_discrete_sequence=px.colors.qualitative.#DC391)

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a INFORMAÇÃO.')

st.plotly_chart(fig, use_container_width=True)

st.caption('PROJETO DESENVOLVIDO POR ALUNOS UNIVESP,EM PROJETO INTEGRADOR. TUPA/SP')
