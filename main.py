import conexao
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Definimos o esquema de dados esperado no POST
class FarmaceuticoSchema(BaseModel):
    nome: str
    crf: str  # Ajuste os campos de acordo com a sua tabela

@app.get("/farmaceuticos")
def lista():
    return conexao.listar()

# 1. GET /farmaceuticos/{id}
@app.get("/farmaceuticos/{id}")
def busca_por_id(id: int):
    resultado = conexao.buscar_por_id(id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Farmacêutico não encontrado")
    return resultado

# 2. POST /farmaceuticos
@app.post("/farmaceuticos", status_code=201)
def cria(farmaceutico: FarmaceuticoSchema):
    try:
        # Converte o modelo do Pydantic em um dicionário do Python
        dados_dict = farmaceutico.model_dump() 
        conexao.inserir(dados_dict)
        return {"mensagem": "Cadastrado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao cadastrar: {str(e)}")

# 3. GET /resumo
@app.get("/resumo")
def resumo():
    return conexao.obter_resumo()
