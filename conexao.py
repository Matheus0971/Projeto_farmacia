from sqlalchemy import create_engine, text
import banco

a = banco.engine

# GET /farmaceuticos
def listar():
    with a.connect() as conexao:
        resposta = conexao.execute(text("SELECT * FROM farmaceuticos"))
        return list(resposta.mappings())

# GET /farmaceuticos/{id}
def buscar_por_id(id_busca: int):
    with a.connect() as conexao:
        # Usamos :id para evitar ataques de SQL Injection
        query = text("SELECT * FROM farmaceuticos WHERE id = :id")
        resposta = conexao.execute(query, {"id": id_busca}).mappings().first()
        return resposta  # Retorna o dicionário ou None se não existir

# POST /farmaceuticos
def inserir(farmaceutico_dados: dict):
    with a.connect() as conexao:
        # Ajuste os nomes das colunas (nome, crf) conforme o seu banco de dados
        query = text("INSERT INTO farmaceuticos (nome, crf) VALUES (:nome, :crf)")
        conexao.execute(query, farmaceutico_dados)
        conexao.commit() # Importante para salvar as alterações no banco

# GET /resumo
def obter_resumo():
    with a.connect() as conexao:
        # Exemplo: Conta o total de farmacêuticos cadastrados
        query = text("SELECT COUNT(*) as total FROM farmaceuticos")
        resposta = conexao.execute(query).mappings().first()
        return resposta
