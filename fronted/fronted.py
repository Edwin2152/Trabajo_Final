from dash import html
import dash_bootstrap_components as dbc


# importamos enlaces de otras carpetas
from .Estructuras.izquierda import izquierda
from .Estructuras.derecha import derecha
from .Estructuras.inferior import inferior


layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Logo", style={'text-align': 'center'}), md=2, style={'background-color': '#E97132'}),
        dbc.Col(html.H1("Cotizador de vehículos", style={'text-align': 'center'}), md=10,
                style={'background-color': '#155F82'}),
        html.Br(), html.Br(), html.Br(), html.Br(),
        dbc.Col(izquierda, md=6, style={'background-color': '#DCEAF7', 'margin-top':'15px'}),
        dbc.Col(derecha, md=6, style={'background-color': 'white'}),
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(
        ), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
        dbc.Col(inferior, md=12, style={'background-color': '#155F82','margin-top':'15px'}),
    ])
])
