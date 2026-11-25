from mongo_conexao import fichas

fichas.delete_many({})

resultado = fichas.insert_many([
    {"produto_id": 1, "rotulo": "Dipirona Sódica 500 mg", "tipo": "medicamento", "principio_ativo": "dipirona", "dosagem_mg": 500, "tarja": "sem tarja"},
    {"produto_id": 2, "rotulo": "Amoxicilina Genérica 500 mg", "tipo": "medicamento", "principio_ativo": "amoxicilina", "dosagem_mg": 500, "tarja": "vermelha"},
    {"produto_id": 3, "rotulo": "Protetor Solar Facial FPS 50", "tipo": "cosmetico", "fps": 50, "volume_ml": 120},
    {"produto_id": 4, "rotulo": "Escova Dental Sorriso Azul", "tipo": "higiene", "marca": "Sorriso", "cor": "azul"},
    {"produto_id": 5, "rotulo": "Dipirona 500 mg", "tipo": "medicamento", "principio_ativo": "dipirona", "dosagem_mg": 500, "tarja": "sem tarja"},
    {"produto_id": 6, "rotulo": "Amoxicilina 500 mg", "tipo": "medicamento", "principio_ativo": "amoxicilina", "dosagem_mg": 500, "tarja": "vermelha"},
    {"produto_id": 7, "rotulo": "Ibuprofeno 400 mg", "tipo": "medicamento", "principio_ativo": "ibuprofeno", "dosagem_mg": 400, "tarja": "sem tarja"},
    {"produto_id": 8, "rotulo": "Protetor Solar FPS 50", "tipo": "cosmetico", "fps": 50, "volume_ml": 120},
    {"produto_id": 9, "rotulo": "Shampoo Anticaspa", "tipo": "higiene", "marca": "Pura", "volume_ml": 200},
    {"produto_id": 10, "rotulo": "Creme Dental Branqueador", "tipo": "higiene", "marca": "Sorriso", "cor": "branco"},
])

print(len(resultado.inserted_ids), "produtos inseridos com sucesso.")
print("No banco:", fichas.count_documents({}),)