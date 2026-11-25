from mongo_conexao import fichas

r = fichas.update_one(
    {"produto_id": 3},
    {"$set": {"fps": 60}}
)

print(r.matched_count, r.modified_count, "ficha atualizada com sucesso.")

r = fichas.update_many(
    {"tipo": "medicamento"},
    {"$set": {"em_estoque": True}}
)

print(r.modified_count, "fichas atualizadas com sucesso.")

for ficha in fichas.find({}, {"_id": 0}):
    print(ficha)

r = fichas.delete_one({"produto_id": 4})

print(r.deleted_count, "ficha deletada com sucesso.")
print(fichas.count_documents({}), "fichas restantes na coleção.")