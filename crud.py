from sqlalchemy.orm import Session  # Importa Session para gerenciar a conexão com o banco de dados
from .models import Tarefa, Usuario  # Importa os modelos de Tarefa e Usuario definidos no arquivo models
from .schemas import TarefaCreate, TarefaUpdate, UsuarioCreate  # Importa os esquemas de validação para Tarefa e Usuario
from typing import List  # Importa List para tipagem de listas

def criar_tarefa(db: Session, tarefa: TarefaCreate, usuario_id: int):
    # Função para criar uma nova tarefa no banco de dados
    db_tarefa = Tarefa(**tarefa.dict(), usuario_id=usuario_id)  # Cria um objeto Tarefa usando os dados da requisição e o ID do usuário
    db.add(db_tarefa)  # Adiciona o objeto na sessão do banco de dados
    db.commit()  # Confirma as alterações no banco
    db.refresh(db_tarefa)  # Atualiza o objeto com os dados do banco (ex.: ID gerado)
    return db_tarefa  # Retorna a tarefa criada

def listar_tarefas(db: Session) -> List[Tarefa]:
    # Função para listar todas as tarefas
    return db.query(Tarefa).all()  # Consulta e retorna todas as tarefas da tabela

def obter_tarefa(db: Session, tarefa_id: int):
    # Função para obter uma tarefa pelo ID
    return db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()  # Filtra a tarefa pelo ID e retorna a primeira correspondente

def atualizar_tarefa(db: Session, tarefa_id: int, tarefa: TarefaUpdate):
    # Função para atualizar uma tarefa existente
    db_tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()  # Obtém a tarefa pelo ID
    if db_tarefa:  # Verifica se a tarefa foi encontrada
        for key, value in tarefa.dict(exclude_unset=True).items():  # Itera pelos campos a serem atualizados
            setattr(db_tarefa, key, value)  # Atualiza os valores da tarefa
        db.commit()  # Confirma as alterações no banco
        db.refresh(db_tarefa)  # Atualiza o objeto com os dados do banco
    return db_tarefa  # Retorna a tarefa atualizada ou None se não existir

def deletar_tarefa(db: Session, tarefa_id: int):
    # Função para deletar uma tarefa pelo ID
    db_tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()  # Obtém a tarefa pelo ID
    if db_tarefa:  # Verifica se a tarefa foi encontrada
        db.delete(db_tarefa)  # Remove a tarefa da sessão do banco de dados
        db.commit()  # Confirma a exclusão no banco
    return db_tarefa  # Retorna a tarefa excluída ou None se não existir

def criar_usuario(db: Session, usuario: UsuarioCreate):
    # Função para criar um novo usuário no banco de dados
    db_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)  # Cria um objeto Usuario com os dados fornecidos
    db.add(db_usuario)  # Adiciona o objeto na sessão do banco de dados
    db.commit()  # Confirma as alterações no banco
    db.refresh(db_usuario)  # Atualiza o objeto com os dados do banco (ex.: ID gerado)
    return db_usuario  # Retorna o usuário criado
