from fastapi.testclient import TestClient
from banco import Sessao
from main import app
from model import Farmaceutico

client = TestClient(app)


def test_listar_farmaceuticos():
    resposta = client.get("/farmaceuticos")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)


def test_criar_e_buscar_farmaceutico():
    payload = {"nome": "Farmaceutico Teste", "idade": 30}
    criacao = client.post("/farmaceuticos", json=payload)
    assert criacao.status_code == 201
    criado = criacao.json()
    assert criado["nome"] == payload["nome"]
    assert criado["idade"] == payload["idade"]
    assert "id" in criado

    try:
        busca = client.get(f"/farmaceuticos/{criado['id']}")
        assert busca.status_code == 200
        assert busca.json() == criado
    finally:
        with Sessao() as sessao:
            registro = sessao.get(Farmaceutico, criado["id"])
            if registro is not None:
                sessao.delete(registro)
                sessao.commit()


def test_buscar_farmaceutico_inexistente():
    resposta = client.get("/farmaceuticos/999999")
    assert resposta.status_code == 404


def test_resumo():
    resposta = client.get("/resumo")
    assert resposta.status_code == 200
    dados = resposta.json()
    assert "total" in dados
    assert "faturamento_total" in dados
