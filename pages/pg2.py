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

dash.register_page(__name__, path='/pg2', name='Média de Gols')

colors = {
    'background': 'black',
    'text': '#fff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('Mediadegols.csv')

x = df['Edição']
y = df['Gols']

fig, ax = plt.subplots(figsize=(13, 7))

fig = go.Figure()

fig = px.scatter(df, x="Edição", y="Gols", labels={
    'Gols': 'Média',
})
fig.update_xaxes(tick0=1930, dtick=4)
fig.update_traces(mode='lines+markers', line=dict( color='red')) # Deixando o gráfico com linhas e marcadores (por default px.scatter é apenas dispersão e px.lines é apenas linhas)
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
        Média de gols nas Copas
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
                        
                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                ),

                  ]
        ),

        dbc.Row(
            [

     dbc.Col(
                    [
                        dcc.Graph(id='media_de_gols_2',
                        figure=fig)

                    ], width=12
                )

            ]

        )
    
]
)
