import dash, dcc
import dash_bootstrap_components as dbc
from dash import html,dcc
from dash.dependencies import Input, Output

#from backend.base import db

izquierda=dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Seleccione marca"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(['Marca 1','Marca 2', 'Marca 3'],value='Marca 1',),
        dbc.Col(html.H2("Seleccione la referencia"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(['Referencia 1','Referencia 2', 'Referencia 3'],value='Referencia 1',),
        dbc.Col(html.H2("Seleccione el modelo"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(['Modelo 1','Modelo 2', 'Modelo 3'],value='Modelo 1',),
    ])    
])