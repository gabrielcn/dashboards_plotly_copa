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

dash.register_page(__name__, path='/', name='Home')

colors = {
    'background': '#000000',
    'text': '#fff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('Mediadegols.csv')

x = df['Edição']
y = df['Gols']

fig, ax = plt.subplots(figsize=(13, 7))

fig = go.Figure()

opcoes = list(df['Edição'].unique())
opcoes.append("Todas as Edições")

fig = px.bar(df, x="Edição", y="Gols", color="Gols", barmode="group",labels={
        'Edição': 'Edição',
        'Gols': 'Média de gols'
        }, color_continuous_scale=px.colors.sequential.Viridis, text_auto = True)
fig.update_xaxes(tick0=1930, dtick=4)
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
                        dcc.Dropdown(opcoes, value='Todas as Edições', id='lista_copas', style={'backgroundColor': '#E6E6FA'})
                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                ),

                  ]
        ),

        dbc.Row(
            [

     dbc.Col(
                    [
                        dcc.Graph(id='media_de_gols',
                        figure=fig)

                    ], width=12
                )

            ]

        )
    
]
)

@callback(
    Output('media_de_gols', 'figure'),
    Input('lista_copas', 'value')
)
def update_output(value):
    if value == "Todas as Edições":
        fig = px.bar(df, x="Edição", y="Gols", color="Gols", barmode="group",labels={
        'Edição': 'Edição',
        'Gols': 'Média de gols'
        }, color_continuous_scale=px.colors.sequential.Viridis, text_auto = True)
        fig.update_xaxes(tick0=1930, dtick=4)
        fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
        
    else:
        tabela_filtrada = df.loc[df['Edição']==value]
        fig = px.bar(tabela_filtrada, x="Edição", y="Gols", color="Gols", barmode="group", labels={
        'Edição': 'Edição',
        'Gols': 'Média de gols'
        }, color_continuous_scale=px.colors.sequential.Viridis, text_auto = True)
        fig.update_xaxes(tick0=1930, dtick=4)
        fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
    return fig

