from banco import engine
from model import Base
from sqlalchemy import text


Base.metadata.create_all(engine)

print("Tabelas criadas",",".join(Base.metadata.tables))
