from banco import engine
from model import Base

Base.metadata.create_all(engine)

print("Tabelas criadas:", ", ".join(Base.metadata.tables))
