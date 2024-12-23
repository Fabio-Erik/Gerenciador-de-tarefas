from pydantic import BaseModel  
# Importa `BaseModel` do Pydantic, que é usado para validação e definição de esquemas de dados.

from typing import Optional  
# Importa `Optional`, que permite que atributos sejam opcionais.

class TarefaCreate(BaseModel):  
    # Esquema para criar uma nova tarefa.
    descricao: str  
    # Campo obrigatório que define a descrição da tarefa.
    estado: Optional[str] = "pendente"  
    # Campo opcional com valor padrão "pendente", que define o estado da tarefa.

class TarefaOut(TarefaCreate):  
    # Esquema para representar uma tarefa ao enviá-la como resposta.
    id: int  
    # ID único da tarefa.
    usuario_id: int  
    # ID do usuário associado à tarefa.

    class Config:  
        # Configuração adicional para o modelo.
        orm_mode = True  
        # Ativa o modo ORM para que objetos ORM sejam convertidos para o formato do esquema.

class TarefaUpdate(BaseModel):  
    # Esquema para atualizar uma tarefa.
    descricao: Optional[str]  
    # Campo opcional para atualizar a descrição.
    estado: Optional[str]  
    # Campo opcional para atualizar o estado.

class UsuarioCreate(BaseModel):  
    # Esquema para criar um novo usuário.
    nome: str  
    # Campo obrigatório para o nome do usuário.
    email: str  
    # Campo obrigatório para o email do usuário.
    senha: str  
    # Campo obrigatório para a senha do usuário.

class UsuarioOut(UsuarioCreate):  
    # Esquema para representar um usuário ao enviá-lo como resposta.
    id: int  
    # ID único do usuário.

    class Config:  
        # Configuração adicional para o modelo.
        orm_mode = True  
        # Ativa o modo ORM para que objetos ORM sejam convertidos para o formato do esquema.
