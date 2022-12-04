# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
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

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])

sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)


server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Dashboards",
                         style={'fontSize':50, 'textAlign':'center', 'font-weight': 'bold', 'backgroundColor': '#ADD8E6'}))
    ]),

    html.Hr(style={'backgroundColor': '#ADD8E6'}),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2, style={'backgroundColor': '#ADD8E6'}),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10, style={'backgroundColor': '#ADD8E6'})
        ]
    )
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)