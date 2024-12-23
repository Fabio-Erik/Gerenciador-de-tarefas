from sqlalchemy import create_engine  # Importa a função para criar uma conexão com o banco de dados
from sqlalchemy.orm import sessionmaker, Session  # Importa ferramentas para gerenciar sessões do banco de dados
from .models import SQLModel  # Importa a classe base SQLModel que será usada para criar as tabelas

DATABASE_URL = "sqlite:///./todolist.db"  # Define o caminho do banco de dados SQLite

engine = create_engine(DATABASE_URL, echo=True)  
# Cria uma "engine" que gerencia a conexão com o banco de dados. 
# O parâmetro `echo=True` faz o SQLAlchemy exibir no console as consultas realizadas.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Cria uma fábrica de sessões:
# - `autocommit=False`: As alterações não são confirmadas automaticamente.
# - `autoflush=False`: Não sincroniza automaticamente os objetos na sessão com o banco.
# - `bind=engine`: Vincula a fábrica de sessões à "engine" criada.

def get_db():
    # Função para obter uma sessão de banco de dados
    db = SessionLocal()  # Cria uma nova sessão
    try:
        yield db  # Faz a sessão estar disponível para o uso (ex.: em rotas do FastAPI)
    finally:
        db.close()  # Garante que a sessão será fechada após o uso
