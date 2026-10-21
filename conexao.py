from sqlalchemy import create_engine, text
import banco

a = banco.engine

def listar():
    with a.connect() as conexao:
        resposta = conexao.execute(text("SELECT * FROM farmaceuticos"))
        return list(resposta.mappings())

def buscar_por_id(id_busca: int):
    with a.connect() as conexao:

        query = text("SELECT * FROM farmaceuticos WHERE id = :id")
        resposta = conexao.execute(query, {"id": id_busca}).mappings().first()
        return resposta  

def inserir(farmaceutico_dados: dict):
    with a.connect() as conexao:

        query = text("INSERT INTO farmaceuticos (nome, crf) VALUES (:nome, :crf)")
        conexao.execute(query, farmaceutico_dados)
        conexao.commit() 

def obter_resumo():
    with a.connect() as conexao:

        query = text("SELECT COUNT(*) as total FROM farmaceuticos")
        resposta = conexao.execute(query).mappings().first()
        return resposta
