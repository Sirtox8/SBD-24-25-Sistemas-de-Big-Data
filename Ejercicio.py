from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

miquery = { "paginas": 1072 } 

libros = librosColeccion.find(miquery)
for l in libros:
    print(f"Que tenga 1072 paginas {l}")


print ("Libros con precio mayor o igual a 5 y el titulo empiece por 1")
libros = librosColeccion.find({ "$and" : [
                                                     { "titulo" : {"$regex": "^1" }},
                                                     { "precio" : { "$gte":5} }
                                                   ]
                                           }
                                           )
for l in libros:
    print(f"Libros que cumplen: {l}")

print ("Libros que no tengan mas de 600 paginas y no cuestan mas de 30€")
libros= librosColeccion.find({ "$nor" : [
                                                     { "paginas" : {"$gt": 600 }},
                                                     { "precio" : { "$gt":30} }
                                                   ]
                                           }
                                           ).sort("titulo",-1)
print("Listado de libros ordenados por precio descendente")

for l in libros:
    print(f"Libros que cumplen: {l}")

print ("Precio nuevo")
miquery = { "precio": 19.99 }
nuevosValores = { "$set": { "precio": 10.99 } }
resultado = librosColeccion.update_one(miquery, nuevosValores)
for l in libros:
    print ({l})
