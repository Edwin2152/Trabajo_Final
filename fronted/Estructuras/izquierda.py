import dash
import dash_bootstrap_components as dbc
from dash import html,dcc
from dash.dependencies import Input, Output

from backend.base import marcas, referencias, modelos, clases


izquierda=dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Seleccione Categoría"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(options=[{'label': clase, 'value': clase} for clase in clases], value=clases[0], id="Clase_consultada"),
        dbc.Col(html.H2("Seleccione Marca"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(options=[{'label': marca, 'value': marca} for marca in marcas], value=marcas[0], id="Marca_consultado"),
        dbc.Col(html.H2("Seleccione la Referencia"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(options=[{'label': referencia, 'value': referencia} for referencia in referencias], value=referencias[0],id="Referencia_consultado"),
        dbc.Col(html.H2("Seleccione el Modelo"), md=12, style={'background-color': '#155F82','margin-top':'15px'}),
        dcc.Dropdown(options=[{'label': modelo, 'value': modelo} for modelo in modelos], value=modelos[0],id="Modelo_consultado"),
        
        
        
    ])    
])