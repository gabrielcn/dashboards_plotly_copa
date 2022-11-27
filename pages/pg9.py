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

dash.register_page(__name__, path='/pg9', name='Vices')

colors = {
    'background': '#111111',
    'text': '#fff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('Vices.csv')

fig, ax = plt.subplots(figsize=(13, 7))

fig = go.Figure()

opcoes = list(df['Seleção'].unique())
opcoes.append("Todas as Seleções")

fig = px.bar(df, x="Seleção", y="Vices", color="Vices", barmode="group",labels={
        'Campeoes': 'Titulos',
        }, color_continuous_scale=px.colors.sequential.Viridis, text_auto=True)
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
        Vice-Campeões 
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
                        dcc.Graph(id='vices',
                        figure=fig)

                    ], width=12
                )

            ]

        )
    
]
)

@callback(
    Output('vices', 'figure'),
    Input('lista_copas', 'value')
)
def update_output(value):
    if value == "Todas as Seleções":
        fig = px.bar(df, x="Seleção", y="Vices", color="Vices", labels={
        'Vices': 'Vice(s)'
        }, color_continuous_scale=px.colors.sequential.Viridis, text_auto=True)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            )
        
    else:
        tabela_filtrada = df.loc[df['Seleção']==value]
        fig = px.bar(tabela_filtrada, x="Seleção", y="Vices", color="Vices", labels={
        'Vices': 'Vice(s)'
        }, color_continuous_scale=px.colors.sequential.Viridis, text_auto=True)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            )

    return fig