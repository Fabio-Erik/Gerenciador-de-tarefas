from jose import JWTError, jwt  # Importa a biblioteca jose para trabalhar com JWT (JSON Web Tokens)
from datetime import datetime, timedelta  # Importa funções para trabalhar com datas e tempos
from passlib.context import CryptContext  # Importa contexto para criptografar senhas
from typing import Union  # Importa Union para indicar tipos opcionais nas funções

SECRET_KEY = "b9b8c6a3f33b5fcd65898f3b02033bb42d8c6f58c8c859125604b35ca9c15f49" # Define a chave secreta para assinar o JWT
ALGORITHM = "HS256" # Define o algoritmo de assinatura do JWT (HMAC com SHA-256)
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Define o tempo de expiração do token de acesso (30 minutos)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Cria contexto para usar bcrypt na criptografia de senhas

def get_password_hash(password: str):
    # Função que gera um hash (versão criptografada) da senha usando bcrypt
    return pwd_context.hash(password) 

def verify_password(plain_password, hashed_password):
      # Função que verifica se a senha simples corresponde ao hash da senha
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    # Função que cria um token de acesso (JWT)
    if expires_delta:
        expires = datetime.utcnow() + expires_delta () # Se expiração personalizada for passada, usa ela
    else:
        expires = datetime.utcnow() + timedelta(minutes=15) # Se não, define 15 minutos como tempo de expiração
    to_encode = data.copy() # Cria uma cópia dos dados a serem incluídos no token
    to_encode.update({"exp": expires}) # Adiciona o campo de expiração no token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # Codifica o JWT com os dados e chave secreta
    return encoded_jwt # Retorna o JWT gerado

def verify_token(token: str):
     # Função que verifica a validade de um token JWT
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # Tenta decodificar o token usando a chave secreta e o algoritmo
        return payload  # Se o token for válido, retorna os dados decodificados
    except JWTError:
        return None  # Se ocorrer erro (token inválido ou expirado), retorna None
