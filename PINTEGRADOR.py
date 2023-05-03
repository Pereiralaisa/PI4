# -*- coding: utf-8 -*-
"""PI 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tBaEd40s8A6x7tzYH8scGfqUBcyEW8SM
"""

import pandas as pd
import plotly.express as px
import streamlit as st 

#streamlit run codigoBase.py

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','vaccinateds': 'Vacinas aplicadas primeira dose','vaccinated_second': 'Vacinas aplicadas segunda dose','tests': 'Testes Realizados','tests_per_100k_inhabitants': ' Testes por 100 mil Habitantes',})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('ESTADO', SP)

#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Vacinas aplicadas primeira dose','Vacinas aplicadas segunda dose','Testes Realizados',' Testes por 100 mil Habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID-19')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Projeto desenvolvido por alunos UNIVESP,PROJETO INTEGRADOR IV')
