import dash
import dash_bootstrap_components as dbc
from dash import html


#importamos enlaces de otras carpetas
from.Estructuras.izquierda import izquierda
from.Estructuras.derecha import derecha

layout=dbc.Container([
    dbc.Row([
        dbc.Col("logo",md=2,style={'background-color':'blue'}),
        dbc.Col("nombre",md=10,style={'background-color':'purple'}),

html.Br(),html.Br(),html.Br(),html.Br(),
        dbc.Col(izquierda,md=6,style={'background-color':'yellow'}),
        dbc.Col(derecha,md=6,style={'background-color':'gray'}),
        
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),

    ])



])

