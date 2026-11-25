from sqlalchemy import func, select
from banco import Sessao
from model import Farmaceutico, Venda


def _serializar_farmaceutico(farmaceutico: Farmaceutico) -> dict:
    return {
        "id": farmaceutico.id,
        "nome": farmaceutico.nome,
        "idade": farmaceutico.idade,
    }


def listar() -> list[dict]:
    with Sessao() as sessao:
        itens = sessao.scalars(select(Farmaceutico).order_by(Farmaceutico.id)).all()
        return [_serializar_farmaceutico(item) for item in itens]


def buscar_por_id(id_busca: int) -> dict | None:
    with Sessao() as sessao:
        item = sessao.get(Farmaceutico, id_busca)
        if item is None:
            return None
        return _serializar_farmaceutico(item)


def inserir(farmaceutico_dados: dict) -> dict:
    with Sessao() as sessao:
        novo = Farmaceutico(
            nome=farmaceutico_dados["nome"],
            idade=farmaceutico_dados.get("idade"),
        )
        sessao.add(novo)
        sessao.commit()
        sessao.refresh(novo)
        return _serializar_farmaceutico(novo)


def obter_resumo() -> dict:
    with Sessao() as sessao:
        total_farmaceuticos = sessao.scalar(select(func.count(Farmaceutico.id))) or 0
        media_idade = sessao.scalar(select(func.avg(Farmaceutico.idade)))
        total_vendas = sessao.scalar(select(func.count(Venda.id))) or 0
        faturamento_total = sessao.scalar(select(func.sum(Venda.valor_total))) or 0.0
        media_venda = sessao.scalar(select(func.avg(Venda.valor_total))) or 0.0
        return {
            "total": int(total_farmaceuticos),
            "media_idade": round(float(media_idade), 2) if media_idade is not None else None,
            "total_vendas": int(total_vendas),
            "faturamento_total": round(float(faturamento_total), 2),
            "media_venda": round(float(media_venda), 2),
        }
