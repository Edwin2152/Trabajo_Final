import dash
import dash_bootstrap_components as dbc
from dash import html


derecha = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Imagen"), md=12, style={
                'background-color': '#155F82','margin-top':'15px'}),
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(
        ), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),html.Br(),html.Br(),
        dbc.Col([html.H2("Detalle y precio"), html.Hr(), html.Hr(), html.Hr(), html.Hr(), html.Hr(
        ),], md=12, style={'background-color': '#155F82','margin-top':'15px'},),
        dbc.Col(html.H2("Datos de contacto"), md=12,
                style={'background-color': 'gray','margin-top':'15px'}),
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

    ])
])
