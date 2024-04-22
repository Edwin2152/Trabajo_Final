import dash
import dash_bootstrap_components as dbc
from dash import Dash, html,dcc, callback, Input, Output
from pymongo.mongo_client import MongoClient


from backend.base import db

app= dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

from fronted.fronted import layout

app.layout=layout

@callback(
    Output('resultado',"value"),
    Input("Marca_consultado", "value"),
    Input("Referencia_consultado", "value"),
    Input("Modelo_consultado", "value")
)


def consulta(Marca_consultado,Referencia_consultado,Modelo_consultado):
    # Consulta concatenada
    filtro = {
        "Marca":Marca_consultado,
        "Referencia": Referencia_consultado,
        "Modelo": Modelo_consultado
    }

    # Realizar la consulta a la base de datos
    resultado = db.find_One(filtro)

    if resultado:print( "El precio es:",resultado['Precio'])
    else : print ("No se encontraron resultados para los filtros especificados.")



if __name__=='__main__':
    app.run_server(debug=True).,