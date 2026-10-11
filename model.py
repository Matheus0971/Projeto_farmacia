import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

load_dotenv()

# Recupera URL do banco do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///farmacia.db")

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Farmaceutico(Base):
    __tablename__ = "farmaceuticos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    crf = Column(String(20), unique=True, nullable=False)

    # Relacionamento com Venda
    vendas = relationship("Venda", back_populates="farmaceutico")

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)

    # Relacionamento com Venda
    vendas = relationship("Venda", back_populates="cliente")

class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_venda = Column(DateTime, default=datetime.now)
    valor_total = Column(Float, nullable=False)

    # Chaves Estrangeiras
    farmaceutico_id = Column(Integer, ForeignKey("farmaceuticos.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    # Relacionamentos
    farmaceutico = relationship("Farmaceutico", back_populates="vendas")
    cliente = relationship("Cliente", back_populates="vendas")