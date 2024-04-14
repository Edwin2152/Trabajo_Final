import dash
import dash_bootstrap_components as dbc
from dash import html


layout=dbc.Container([
    dbc.Row([
        dbc.Col("izquierda",md=2,style={'background-color':'blue'}),
        dbc.Col("derecha",md=10,style={'background-color':'black'}),

    ])




])