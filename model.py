from datetime import date
import datetime
from typing import Optional
from xmlrpc.client import boolean
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from datetime import date
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)
    rotulo: Mapped[str] = mapped_column(String(200))
    ano: Mapped[int]
    farmaceutico_id: Mapped[int] = mapped_column(ForeignKey("farmaceuticos.id"), index=True)
    farmaceutico: Mapped["Farmaceutico"] = relationship(back_populates="produtos")



class Farmaceutico(Base):
    __tablename__ = "farmaceuticos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    idade: Mapped[int]
    produtos: Mapped[list["Produto"]] = relationship(back_populates="farmaceutico")
