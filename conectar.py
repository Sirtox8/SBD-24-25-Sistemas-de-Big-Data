from pymongo import MongoClient

client = MongoClient('mongodb+srv://Sito:Sitobabaro11!@sito.xlfvv.mongodb.net/?retryWrites=true&w=majority&appName=Sito')

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

cliente = MongoClient('mongodb+srv://'+usuario+':'+password+'@sito.xlfvv.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)
try:
   cliente.admin.command('ping')
   print("NOS CONECTAMOS CORRECTAMENTE")
except Exception as e:
   print(e)

