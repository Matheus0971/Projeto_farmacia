from typing import Optional
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Farmaceutico(Base):
    __tablename__ = "farmaceuticos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    idade: Mapped[Optional[int]]
    produtos: Mapped[list["Produto"]] = relationship(back_populates="farmaceutico")
    vendas: Mapped[list["Venda"]] = relationship(back_populates="farmaceutico")


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)
    rotulo: Mapped[str] = mapped_column(String(200))
    ano: Mapped[Optional[int]]
    farmaceutico_id: Mapped[int] = mapped_column(ForeignKey("farmaceuticos.id"), index=True)
    farmaceutico: Mapped["Farmaceutico"] = relationship(back_populates="produtos")
    vendas: Mapped[list["Venda"]] = relationship(back_populates="produto")


class Venda(Base):
    __tablename__ = "vendas"

    id: Mapped[int] = mapped_column(primary_key=True)
    farmaceutico_id: Mapped[int] = mapped_column(ForeignKey("farmaceuticos.id"), index=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"), index=True)
    quantidade: Mapped[int] = mapped_column(Integer)
    valor_total: Mapped[float] = mapped_column(Float)
    farmaceutico: Mapped["Farmaceutico"] = relationship(back_populates="vendas")
    produto: Mapped["Produto"] = relationship(back_populates="vendas")
