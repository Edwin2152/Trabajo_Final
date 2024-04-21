import dash
import dash_bootstrap_components as dbc
from dash import Dash, html,dcc, callback, Input, Output
from pymongo.mongo_client import MongoClient


from backend.base import db

app= dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

from fronted.fronted import layout

app.layout=layout

#@callback(
    #Output(),
    #Input("Marca_consultado", "value"),
    #Input("Referencia_consultado", "value"),
    #Input("Modelo_consultado", "value")
#)

#def consulta(auto_consultado,Referencia_consultado,Modelo_consultado):
    # Consulta concatenada
    #filtro = {
       # "Marca": auto_consultado,
        #"Referencia": Referencia_consultado,
        #"Modelo": Modelo_consultado
   # }

    # Realizar la consulta a la base de datos
    #resultados = db.find(filtro)

    # Convertir los resultados a una lista
    #print(dataframe(resultados))

   #resultado = dataframe["Precio"]
    #return

if __name__=='__main__':
    app.run_server(debug=True)