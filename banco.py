import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

SERVIDOR = (f"postgresql+psycopg://{os.environ['PGUSER']}:{os.environ['PGPASSWORD']}"
            f"@{os.environ['PGHOST']}:{os.environ['PGPORT']}")

URL = SERVIDOR + "/farmacia"

engine = create_engine(URL, echo=False)
Sessao = sessionmaker(bind=engine)
