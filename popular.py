from sqlalchemy import delete, insert
from banco import Sessao
from model import Farmaceutico, Produto, Venda

FARMACEUTICOS = [
    {"nome": "Ana Paula", "idade": 34},
    {"nome": "Carlos Eduardo", "idade": 41},
    {"nome": "Fernanda Lima", "idade": 29},
    {"nome": "João Pedro", "idade": 37},
    {"nome": "Mariana Souza", "idade": 31},
    {"nome": "Rafael Costa", "idade": 45},
]

PRODUTOS = [
    {"rotulo": "Dipirona Sódica 500 mg", "ano": 2026, "f_idx": 0},
    {"rotulo": "Amoxicilina Genérica 500 mg", "ano": 2026, "f_idx": 1},
    {"rotulo": "Protetor Solar Facial FPS 50", "ano": 2026, "f_idx": 2},
    {"rotulo": "Escova Dental Sorriso Azul", "ano": 2025, "f_idx": 3},
    {"rotulo": "Dipirona 500 mg", "ano": 2026, "f_idx": 0},
    {"rotulo": "Amoxicilina 500 mg", "ano": 2026, "f_idx": 1},
    {"rotulo": "Ibuprofeno 400 mg", "ano": 2026, "f_idx": 4},
    {"rotulo": "Protetor Solar FPS 50", "ano": 2026, "f_idx": 2},
    {"rotulo": "Shampoo Anticaspa", "ano": 2025, "f_idx": 5},
    {"rotulo": "Creme Dental Branqueador", "ano": 2025, "f_idx": 3},
    {"rotulo": "Paracetamol 750 mg", "ano": 2026, "f_idx": 0},
    {"rotulo": "Vitamina C 1 g", "ano": 2026, "f_idx": 4},
    {"rotulo": "Álcool Gel 70%", "ano": 2025, "f_idx": 5},
    {"rotulo": "Omeprazol 20 mg", "ano": 2026, "f_idx": 1},
    {"rotulo": "Loratadina 10 mg", "ano": 2026, "f_idx": 2},
]

VENDAS = [
    (0, 0, 5, 62.50),
    (0, 4, 4, 44.00),
    (0, 10, 3, 54.00),
    (0, 11, 2, 78.00),
    (1, 1, 6, 210.00),
    (1, 5, 5, 165.00),
    (1, 13, 4, 112.00),
    (1, 6, 3, 72.00),
    (2, 2, 8, 520.00),
    (2, 7, 6, 450.00),
    (2, 14, 4, 96.00),
    (2, 11, 5, 195.00),
    (2, 0, 4, 50.00),
    (3, 3, 5, 65.00),
    (3, 9, 4, 52.00),
    (3, 12, 6, 84.00),
    (3, 4, 3, 33.00),
    (4, 6, 7, 168.00),
    (4, 11, 6, 234.00),
    (4, 2, 4, 260.00),
    (4, 10, 5, 90.00),
    (5, 8, 4, 136.00),
    (5, 12, 5, 70.00),
    (5, 13, 3, 84.00),
]

with Sessao() as sessao:
    sessao.execute(delete(Venda))
    sessao.execute(delete(Produto))
    sessao.execute(delete(Farmaceutico))

    f_ids = sessao.scalars(
        insert(Farmaceutico).returning(Farmaceutico.id),
        FARMACEUTICOS,
    ).all()

    produtos_payload = [
        {"rotulo": p["rotulo"], "ano": p["ano"], "farmaceutico_id": f_ids[p["f_idx"]]}
        for p in PRODUTOS
    ]
    p_ids = sessao.scalars(
        insert(Produto).returning(Produto.id),
        produtos_payload,
    ).all()

    vendas_payload = [
        {
            "farmaceutico_id": f_ids[f_idx],
            "produto_id": p_ids[p_idx],
            "quantidade": qtd,
            "valor_total": valor,
        }
        for f_idx, p_idx, qtd, valor in VENDAS
    ]
    sessao.execute(insert(Venda), vendas_payload)
    sessao.commit()

    print(
        f"Inseridos: {len(f_ids)} farmaceuticos, "
        f"{len(p_ids)} produtos e {len(vendas_payload)} vendas."
    )
