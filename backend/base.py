from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://eaar2152:1234@cluster0.bwiiq7q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
db=client.Base

