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

dash.register_page(__name__, path='/pg10', name='Ranking')

colors = {
    'background': '#111111',
    'text': '#fff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('fifa_ranking-2022.csv')

fig, ax = plt.subplots(figsize=(13, 7))

fig = go.Figure()

opcoes = list(df['country_full'].unique())
opcoes.append("Todas as Seleções")

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Copa do Mundo FIFA',
    style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Ranking Geral da FIFA 2022 
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
                        dcc.Graph(id='ranking',
                        figure=fig)

                    ], width=12
                )

            ]

        )
    
]
)

@callback(
    Output('ranking', 'figure'),
    Input('lista_copas', 'value')
)
def update_output(value):
    if value == "Todas as Seleções":
        fig = px.bar(df, x="country_full", y="total_points", color="total_points", hover_name='rank', labels={
        'rank': 'Posição',
        'country_full': 'País',
        'total_points': 'Pontos totais',
        'confederation': 'Confederação'
        }, color_continuous_scale=px.colors.sequential.Cividis, text_auto=True)
        fig.update_yaxes(tickvals=[0, 500, 1000, 1400, 1800])
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            )
        fig.update_xaxes(tickangle=45)
        
    else:
        tabela_filtrada = df.loc[df['country_full']==value]
        fig = px.bar(tabela_filtrada, x="country_full", y="total_points", color="total_points", hover_name='rank', labels={
        'country_full': 'País',
        'total_points': 'Pontos totais',
        'confederation': 'Confederação'
        }, color_discrete_sequence= px.colors.sequential.Plasma_r, text_auto=True)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            )

    return fig