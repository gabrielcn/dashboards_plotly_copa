from dash import Dash, html, dcc, Input, Output, callback
import dash
import plotly.graph_objects as go
import plotly.express as px
import os
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/pg8', name='Campeões')

colors = {
    'background': '#111111',
    'text': '#fff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('Campeoes.csv')

fig, ax = plt.subplots(figsize=(13, 7))

fig = go.Figure()

opcoes = list(df['Selecoes'].unique())
opcoes.append("Todas as Seleções")

fig = px.bar(df, x="Selecoes", y="Campeoes", color="Campeoes", labels={
        'Campeoes': 'Titulo(s)',
        }, color_discrete_sequence=px.colors.qualitative.Prism, text_auto=True)
fig.update_layout(
plot_bgcolor=colors['background'],
paper_bgcolor=colors['background'],
font_color=colors['text'])

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Copa do Mundo FIFA',
    style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Campeões 
    ''',
    style={
        'textAlign': 'center',
        'color': colors['text']
    }
    
    
    ),

     dbc.Row(
            [

    dbc.Col(
                    [
                        dcc.Dropdown(opcoes, value='Todas as Seleções', id='lista_copas')
                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                ),

                  ]
        ),

        dbc.Row(
            [

     dbc.Col(
                    [
                        dcc.Graph(id='campeoes',
                        figure=fig)

                    ], width=12
                )

            ]

        )
    
]
)

@callback(
    Output('campeoes', 'figure'),
    Input('lista_copas', 'value')
)
def update_output(value):
    if value == "Todas as Seleções":
        fig = px.bar(df, x="Selecoes", y="Campeoes", color="Campeoes", labels={
        'Selecoes': 'Seleção',
        'Campeoes': 'Titulo(s)'
        }, color_discrete_sequence=px.colors.qualitative.Prism, text_auto=True)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            )
        
    else:
        tabela_filtrada = df.loc[df['Selecoes']==value]
        fig = px.bar(tabela_filtrada, x="Selecoes", y="Campeoes", color="Campeoes", labels={
        'Campeoes': 'Titulo(s)'
        }, color_discrete_sequence=px.colors.qualitative.Prism, text_auto=True)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            )

    return fig