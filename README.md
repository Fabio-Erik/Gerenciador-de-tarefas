# Gerenciador-de-tarefas
Diretórios que compõem as clausulas para o desafio.

# Desafio Têcnico
Esse é um projeto back-end criado em Python, usando o banco de dados SQLite, e o sistema de FastAPI que é um framework que permite a criação de APIs de uma forma mais rapida e eficiente. Esse projeto permite ao usuario gerenciar suas tarefas sejam elas quais forem, e também inicialmente criar uma conta onde poderá armazenar suas tarefas deixando assim seu progresso salvo.

# Funcionalidades
- Registrar um usuário.
- Fazer login para obter o token.
- Adicionar, editar e remover tarefas;
- Listar todas as tarefas existentes
- Marcar tarefas como concluidas
- Adicionar prioridade ou urgencia em uma tarefa especifica.

 # Tecnologias utilizadas
- **Python**
- **FastAPI**
- **SQLite**
- **SQLModel** 

# Como instalar

1 - Clone o repositorio de :
 https://github.com/Fabio-Erik/Gerenciador-de-tarefas

2 - Entre na pasta do projeto:
(Possivel caminho - pois isso dependerá de onde os **Dowloads** estão sendo armazenados em seu computador)
Este Computador/Dowloads/

3 - Crie e ative um ambiente virtual:
Cole estes comando em um terminal de uma IDE em opração
python -m venv venv
source venv/bin/activate - No Windows: *venv/bin/activate*

4 - Instale as dependências:
Copie o comando e cole no terminal da sua IDE de python
pip install -r requirements.txt

# Como usar
1 - Execute o servidor:
Copie o comando e cole no terminal da sua IDE de python
uvicorn main:app --reload

2 - Acesse a aplicação no navegador:
ao acessar este endereço você terá acesso a pagina inicial do sitema.
http://127.0.0.1:8000

3 - Para utilizar as aplicações no navegador:
. Acesse o endereço, "http://127.0.0.1:8000/dosc", assim será direcionado para a pagina onde está localizado as endpoints.
. A API pode ser acessada e testada via Swagger UI, assim poderá acessar a interface interativa para utilizar as endpoits.

# Contribuições:
Contribuições são bem vindas! Por favor, abra uma issue ou envie um pull request.

# Licença
Este projeto está licenciado sob a licença MIT(Massachusetts Innstitute of Technology), que é uma  licença permissiva e popular no GitHub que permite que o software seja licenciado de forma open source.
