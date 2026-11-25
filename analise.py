import matplotlib.pyplot as plt
import pandas as pd
from banco import engine

vendas = pd.read_sql("SELECT * FROM vendas", engine)
vendedores = pd.read_sql(
    "SELECT id AS farmaceutico_id, nome AS vendedor FROM farmaceuticos",
    engine,
)
df = vendas.merge(vendedores, on="farmaceutico_id")
faturamento = df.groupby("vendedor")["valor_total"].sum().sort_values(ascending=False)

campeao = faturamento.index[0]
valor = faturamento.iloc[0]
percentual = valor / faturamento.sum() * 100
print(f"{campeao} é o vendedor que mais vendeu: R$ {valor:.2f} ({percentual:.1f}% do total).")

faturamento.head(5).plot.bar(
    title=f"Quem mais vendeu: {campeao} (top 5, em R$)",
    rot=30,
)
plt.ylabel("R$")
plt.tight_layout()
plt.show()
