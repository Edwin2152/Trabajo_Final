
#SE REALIZA CONEXIÓN GENERAL A LA BASE DE DATOS
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://mejiatatiana823:1234@cluster0.kwawjut.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

#CONEXIÓN PUNTUAL A LA BD
db=client['base_autos']
collection = db['base']

#MAGICAMENTE SE EXTRAE LOS VALORES CONSULTADOS POR DEFECTO
marcas = collection.distinct('marca')
referencias = collection.distinct('referencia3')
modelos= collection.distinct('anio')
clases= collection.distinct('clase')




def consultaResultado(Clase_consultada,Marca_consultado,Referencia_consultado,Modelo_consultado):
    print(Clase_consultada,Marca_consultado,Referencia_consultado,Modelo_consultado)
    
    #SE REALIZA CONSULTA PARA EXTRAER EL PRECIO
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
        return precio
    else:
        return "no se encuentra resultado"




# consulta = list(collection.find())
# #crear lista y su respectivo diccionario 
# resultado_tabla = []
# for i in consulta:
#     fila = {
#         "marca" :i["marca"],
#         "referencia3" :i["referencia3"],
#         "anio" :i["anio"],
#         "clase": i["clase"],            
#         "precio" :i["precio"]
#     }
#     resultado_tabla.append(fila)

# return resultado_tabla