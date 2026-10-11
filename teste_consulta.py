from model import SessionLocal, Venda

session = SessionLocal()

# Conta total de vendas
total_vendas = session.query(Venda).count()
print(f"Total de vendas registradas: {total_vendas}\n")

# Lista os 5 primeiros registros com relacionamentos
vendas = session.query(Venda).limit(5).all()

print("--- Primeiras 5 Vendas ---")
for v in vendas:
    print(f"Venda ID: {v.id} | Valor: R$ {v.valor_total:.2f} | Cliente: {v.cliente.nome} | Farmacêutico: {v.farmaceutico.nome}")

session.close()