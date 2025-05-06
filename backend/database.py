from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Criação do banco SQLite
DATABASE_URL = "sqlite:///./docs.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Tabela documentos
class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, nullable=True)
    data = Column(String, nullable=True)
    valor_total = Column(String, nullable=True)
    json_extraido = Column(Text, nullable=True)
    caminho_pdf = Column(String, nullable=False)
    data_upload = Column(DateTime, default=datetime.utcnow)

# Criar a tabela no banco
Base.metadata.create_all(bind=engine)
