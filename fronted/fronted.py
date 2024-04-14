import dash
import dash_bootstrap_components as dbc
from dash import html

#importamos enlaces de otras carpetas
from fronted.derecha import layout


layout=dbc.Container([
    dbc.Row([
        dbc.Col("izquierda",md=2,style={'background-color':'blue'}),
        dbc.Col("derecha",md=10,style={'background-color':'black'}),
html.Br(),html.Br(),html.Br(),html.Br(),
        dbc.Col("izquierda",md=6,style={'background-color':'yellow'}),
        dbc.Col("izquierda",md=6,style={'background-color':'blue'}),
    ])



])

