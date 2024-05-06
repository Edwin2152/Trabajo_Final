import dash
import dash_bootstrap_components as dbc
from dash import Dash, html,dcc, callback, Input, Output
from pymongo.mongo_client import MongoClient
from fronted.fronted import layout
from backend.base import db, consultaResultado

app= dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
app.layout=layout


@callback(
    Output('ResultadoObtenido',"children"),
    Input("Clase_consultada", "value"),
    Input("Marca_consultado", "value"),
    Input("Referencia_consultado", "value"),
    Input("Modelo_consultado", "value")
)


def consulta(Clase_consultada,Marca_consultado,Referencia_consultado,Modelo_consultado): 
    print(Clase_consultada,Marca_consultado,Referencia_consultado,Modelo_consultado)
    return consultaResultado(Clase_consultada,Marca_consultado,Referencia_consultado,Modelo_consultado)
    

if __name__=='__main__':
    app.run_server(debug=True)