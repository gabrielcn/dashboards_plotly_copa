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

dash.register_page(__name__, path='/pg11', name='Mapa')

colors = {
    'background': 'black',
    'text': '#fff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('fifa_ranking-2022.csv')

fig, ax = plt.subplots(figsize=(13, 7))

fig = go.Figure()

fig = px.choropleth(df, locations='country_abrv', color='rank', hover_name='country_full', labels={
        'rank': 'Posição',
        'country_abrv': 'País',
        }, color_continuous_scale=px.colors.sequential.Cividis_r, projection='orthographic')

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Copa do Mundo FIFA',
    style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
       Ranking
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
                        dcc.Graph(id='mapa',
                        figure=fig)

                    ], width=12
                )

            ]

        )
    
]
)
