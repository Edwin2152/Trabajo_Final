
# SE REALIZA CONEXIÓN GENERAL A LA BASE DE DATOS
from pymongo.mongo_client import MongoClient
import locale
uri = "mongodb+srv://mejiatatiana823:1234@cluster0.kwawjut.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

# CONEXIÓN PUNTUAL A LA BD
db = client['base_autos']
collection = db['base']

# SE EXTRAE LOS VALORES CONSULTADOS POR DEFECTO
marcas = collection.distinct('marca')
referencias = collection.distinct('referencia3')
modelos = collection.distinct('anio')
clases = collection.distinct('clase')


def consultaResultado(Clase_consultada, Marca_consultado, Referencia_consultado, Modelo_consultado):
    print(Clase_consultada, Marca_consultado,
          Referencia_consultado, Modelo_consultado)

    # SE REALIZA CONSULTA PARA EXTRAER EL PRECIO
    filtro = {
        'marca': Marca_consultado,
        'referencia3': Referencia_consultado,
        'anio':  Modelo_consultado,
        'clase':  Clase_consultada
    }

    resultados = collection.find_one(filtro)
    print(resultados)

    if resultados:
        precio = resultados.get("precio")
        return "$ "+"{:,}".format(precio*1000)
    else:
        return "no se encuentra resultado"
