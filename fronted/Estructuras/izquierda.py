import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

izquierda=dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Seleccione marca"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),




        
        dbc.Col(html.H2("Seleccione la referencia"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dbc.Col(html.H2("Seleccione el modelo"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dbc.Col(html.H4("Cotizar"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
    ])    
])