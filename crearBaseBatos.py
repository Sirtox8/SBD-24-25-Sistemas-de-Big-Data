from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

clienteMDB= MongoClient('mongodb+srv://'+usuario+':'+password+'@sito.xlfvv.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)

baseDatos = clienteMDB['AlfonsoNogueraNumancia']

coleccion = baseDatos["Miprimeracoleccion"]

documento = {'nombre' : 'Alfonso',
             'apellido' : 'Noguera'
}

insercion = coleccion.insert_one(documento)