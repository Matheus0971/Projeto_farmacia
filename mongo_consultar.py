from mongo_conexao import fichas

linha = "=" * 70

resultado = fichas.find(
    {"tipo": "medicamento"},
    {"_id": 0, "produto_id": 1, "principio_ativo": 1}
)

for ficha in resultado:
    print(ficha)

print(linha)
print(fichas.find_one({"produto_id": 3}, {"_id": 0}))
print(linha)

print("Medicamentos:", fichas.count_documents({"tipo": "medicamento"}))

print("Produtos com ID 1, 4 ou 7:",
      fichas.count_documents({"produto_id": {"$in": [1, 4, 7]}}))