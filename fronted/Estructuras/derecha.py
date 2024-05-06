import dash
import dash_bootstrap_components as dbc
from dash import html,dcc

derecha = dbc.Container([
    dbc.Row([
        dbc.Col([
                html.H2("Detalle y precio:"),
                html.Br(),
                html.Br(),
                html.H2(id="ResultadoObtenido"),
            ],
            md=12, style={'background-color': '#155F82', 'margin-top': '15px'},
        ),        
        dbc.Col(html.Div(id='resultado'), md=12, style={'background-color': '#155F82', 'margin-top': '15px'},),
        
        dbc.Col([html.H2("Datos de contacto"),
                 html.H4("Tatiana Mejia Contacto:3211234567"),
                 html.H4("Edwin Amortegui Contacto:3211234567"),
                 html.H4("Felipe Fonseca Contacto:3211234567 ")], md=12,
                style={'background-color': 'gray', 'margin-top': '15px'},
),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        


    ])
])
