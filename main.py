from fastapi import FastAPI, Depends, HTTPException, status, Query   # type: ignore
# Importa módulos do FastAPI para criar a API, gerenciar dependências e lidar com erros e validações.

from sqlalchemy.orm import Session   # type: ignore
# Importa a classe para gerenciar sessões do banco de dados.

from .models import Tarefa, Usuario  
# Importa os modelos do banco de dados.

from .schemas import TarefaCreate, TarefaOut, TarefaUpdate, UsuarioCreate, UsuarioOut  
# Importa os esquemas usados para validação e retorno de dados.

from .crud import criar_tarefa, listar_tarefas, obter_tarefa, atualizar_tarefa, deletar_tarefa, criar_usuario  
# Importa as funções CRUD (Create, Read, Update, Delete) para manipular os dados.

from .auth import create_access_token, verify_password, get_password_hash  
# Importa funções de autenticação para criar tokens e gerenciar senhas.

from .database import get_db  
# Importa a função para obter a sessão do banco de dados.

from fastapi.security import OAuth2PasswordBearer   # type: ignore
# Importa um esquema de segurança OAuth2 para autenticação baseada em tokens.

app = FastAPI()  
# Inicializa a aplicação FastAPI.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  
# Configura o esquema OAuth2 para autenticação usando o endpoint "/login".

@app.post("/login")  
# Define o endpoint de login com o método HTTP POST.
def login(email: str, senha: str, db: Session = Depends(get_db)):  
    # Função para autenticar um usuário com email e senha.
    usuario = db.query(Usuario).filter(Usuario.email == email).first()  
    # Busca o usuário no banco de dados pelo email.
    if not usuario or not verify_password(senha, usuario.senha):  
        # Verifica se o usuário existe e se a senha está correta.
        raise HTTPException(status_code=401, detail="Credenciais inválidas")  
        # Retorna erro 401 se as credenciais forem inválidas.
    access_token = create_access_token(data={"sub": usuario.email})  
    # Cria um token de acesso para o usuário autenticado.
    return {"access_token": access_token, "token_type": "bearer"}  
    # Retorna o token gerado.

@app.post("/usuario/", response_model=UsuarioOut)  
# Define o endpoint para registrar um novo usuário.
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):  
    # Função para criar um novo usuário no banco de dados.
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()  
    # Verifica se o email já está cadastrado.
    if db_usuario:  
        raise HTTPException(status_code=400, detail="Email já cadastrado")  
        # Retorna erro 400 se o email já estiver em uso.
    usuario_hash = get_password_hash(usuario.senha)  
    # Gera o hash da senha.
    db_usuario = Usuario(**usuario.dict(), senha=usuario_hash)  
    # Cria uma nova instância do usuário com os dados fornecidos e a senha criptografada.
    db.add(db_usuario)  
    # Adiciona o usuário ao banco de dados.
    db.commit()  
    # Salva as alterações no banco de dados.
    db.refresh(db_usuario)  
    # Atualiza o estado da instância com os dados salvos.
    return db_usuario  
    # Retorna o usuário criado.

@app.post("/tarefas/", response_model=TarefaOut)  
# Define o endpoint para criar uma nova tarefa.
def criar_tarefa_endpoint(tarefa: TarefaCreate, db: Session = Depends(get_db)):  
    # Função para criar uma tarefa no banco de dados.
    usuario_id = 1  # Aqui você deve obter o usuário logado.
    db_tarefa = criar_tarefa(db, tarefa, usuario_id)  
    # Chama a função CRUD para criar a tarefa.
    return db_tarefa  
    # Retorna a tarefa criada.

@app.get("/tarefas/", response_model=list[TarefaOut])  
# Define o endpoint para listar todas as tarefas.
def listar_tarefas_endpoint(db: Session = Depends(get_db)):  
    return listar_tarefas(db)  
    # Retorna a lista de tarefas.

@app.get("/tarefas/{tarefa_id}", response_model=TarefaOut)  
# Define o endpoint para visualizar uma tarefa específica.
def visualizar_tarefa_endpoint(tarefa_id: int, db: Session = Depends(get_db)):  
    db_tarefa = obter_tarefa(db, tarefa_id)  
    # Busca a tarefa pelo ID.
    if db_tarefa is None:  
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")  
        # Retorna erro 404 se a tarefa não existir.
    return db_tarefa  
    # Retorna a tarefa encontrada.

@app.put("/tarefas/{tarefa_id}", response_model=TarefaOut)  
# Define o endpoint para atualizar uma tarefa.
def atualizar_tarefa_endpoint(tarefa_id: int, tarefa: TarefaUpdate, db: Session = Depends(get_db)):  
    db_tarefa = atualizar_tarefa(db, tarefa_id, tarefa)  
    # Chama a função CRUD para atualizar a tarefa.
    if db_tarefa is None:  
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")  
        # Retorna erro 404 se a tarefa não existir.
    return db_tarefa  
    # Retorna a tarefa atualizada.

@app.delete("/tarefas/{tarefa_id}", response_model=TarefaOut)  
# Define o endpoint para deletar uma tarefa.
def deletar_tarefa_endpoint(tarefa_id: int, db: Session = Depends(get_db)):  
    db_tarefa = deletar_tarefa(db, tarefa_id)  
    # Chama a função CRUD para deletar a tarefa.
    if db_tarefa is None:  
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")  
        # Retorna erro 404 se a tarefa não existir.
    return db_tarefa  
    # Retorna a tarefa deletada.

@app.get("/")
def read_root():
    return {"Gerenciador de tarefas":"Bem-vindo à API ToDoList!"}
