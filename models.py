from sqlmodel import SQLModel, Field  
# Importa a classe base `SQLModel` e `Field` para definir os modelos do banco de dados.

class Usuario(SQLModel, table=True):  
    # Define o modelo para a tabela de usuários.
    id: int = Field(default=None, primary_key=True)  
    # Define a coluna `id` como chave primária, com valor padrão `None`.
    nome: str  
    # Define a coluna `nome` para armazenar o nome do usuário.
    email: str  
    # Define a coluna `email` para armazenar o email do usuário.
    senha: str  
    # Define a coluna `senha` para armazenar a senha (criptografada) do usuário.

class Tarefa(SQLModel, table=True):  
    # Define o modelo para a tabela de tarefas.
    id: int = Field(default=None, primary_key=True)  
    # Define a coluna `id` como chave primária, com valor padrão `None`.
    descricao: str  
    # Define a coluna `descricao` para armazenar a descrição da tarefa.
    estado: str = "pendente"  
    # Define a coluna `estado` com valor padrão "pendente".
    usuario_id: int = Field(foreign_key="usuario.id")  
    # Define a coluna `usuario_id` como chave estrangeira que referencia a tabela `usuario`.
