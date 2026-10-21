"""Carga de teste: mil autores e 100 mil livros, para o indice ter o que medir."""
import time
from sqlalchemy import delete, insert, text
from banco import Sessao
from model import Produto, Farmaceutico

with Sessao() as sessao:
    sessao.execute(delete(Produto).where(Produto.rotulo.like("Carga %")))
    sessao.execute(delete(Farmaceutico).where(Farmaceutico.nome.like("Farmaceutico %")))

    farmaceuticos = [{"nome": f"Farmaceutico {n}", "idade":n} for n in range(20)]
    ids = sessao.scalars(insert(Farmaceutico).returning(Farmaceutico.id), farmaceuticos).all()

    produtos = [{"rotulo": f"Carga {n}", "ano": 2000, "farmaceutico_id": ids[n % 20]}
              for n in range(100)]
    inicio = time.perf_counter()
    sessao.execute(insert(Produto), produtos)
    sessao.commit()
    print(f"100 mil produtos gravados em {time.perf_counter() - inicio:.1f} s")
    sessao.execute(text("ANALYZE produtos")) #