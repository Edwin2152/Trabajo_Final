from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://mejiatatiana823:1234@cluster0.kwawjut.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
db=client['base_autos']
collection = db['base']

marcas = collection.distinct('marca')
referencias = collection.distinct('referencia3')
modelos= collection.distinct('anio')
clases= collection.distinct('clase')

filtro = {
    'marca': {'$in': marcas},
    'referencia3': {'$in': referencias},
    'anio': {'$in': modelos},
    'clase': {'$in': clases},
    'precio': {'$exists': True}
}


resultados = collection.find(filtro,)

precios = [resultado['precio'] for resultado in resultados]

for resultado in resultados:
    print(resultado)