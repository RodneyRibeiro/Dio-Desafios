"""Desafio Dio, criar conexão e utilizar o MongoDB
"""
import datetime
import pymongo as pym

print(f'Versão Pymongo: {pym.__version__}\n')

client = pym.MongoClient("mongodb+srv://rodneygribeiro:H_2U-VAGUDnGFpG@clusterrodfree.ysem0sq.mongodb.net/")

db = client.test
collection = db.test_collection

print(db.list_collection_names,"\n")
print(db.test_collection,"\n")

# Definir o arquivo
post = {
    "author" : "Mike",
    "text" : "Teste de inserção de dados",
    "tags" : ["mongodb","python3","pymongo"],
    "date" : datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)