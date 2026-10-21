import conexao
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class FarmaceuticoSchema(BaseModel):
    nome: str
    crf: str  

@app.get("/farmaceuticos")
def lista():
    return conexao.listar()

@app.get("/farmaceuticos/{id}")
def busca_por_id(id: int):
    resultado = conexao.buscar_por_id(id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Farmacêutico não encontrado")
    return resultado

@app.post("/farmaceuticos", status_code=201)
def cria(farmaceutico: FarmaceuticoSchema):
    try:
        dados_dict = farmaceutico.model_dump() 
        conexao.inserir(dados_dict)
        return {"mensagem": "Cadastrado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao cadastrar: {str(e)}")

@app.get("/resumo")
def resumo():
    return conexao.obter_resumo()
