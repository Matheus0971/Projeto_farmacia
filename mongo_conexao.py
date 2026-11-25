import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

cliente = MongoClient(os.environ["MONGO_URI"])

print("Servidor rodando. Versão:", cliente.server_info()["version"])

banco = cliente["farmacia"]
fichas = banco["fichas"]

print("Coleções:", banco.list_collection_names())