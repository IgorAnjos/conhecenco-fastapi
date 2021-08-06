#Importando a classe FastAPI do modulo fastapi
from fastapi import FastAPI

#Criar uma aplicação
app = FastAPI()

#Criando uma rota padrao
@app.get('/')       #Decorando uma function
def index():
    return { "resultado": "Está no ar Api em Python !"}

@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, tudo bem?'
    return { "mensagem": texto }

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    return f'O quadrado de {numero} é {resultado}'

@app.get('/profile')
def profile(nome: str):
    return { "Nome": nome}

@app.post('/profile')
def signup(nome):
    return { "mensagem": "Perfil criado com sucesso"}

@app.put('/profile')
def atualizar(nome):
    return { "mensagem": "Perfil atualizado com sucesso"}

@app.delete('/profile')
def remover(nome):
    return { "mensagem": "Perfil deletado com sucesso"}
