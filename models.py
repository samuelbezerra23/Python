from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuração do aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição do modelo de missão espacial
class mission (db.Model):
    __tablename__ = 'missoes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_lancamento = db.Column(db.Date, nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    estado_missao = db.Column(db.String(50), nullable=False)
    tripulacao = db.Column(db.String(200), nullable=True)
    carga_util = db.Column(db.String(500), nullable=True)
    duracao = db.Column(db.String(50), nullable=True)
    custo = db.Column(db.Float, nullable=True)
    detalhes_status = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f" mission  {self.nome}>"

# Criação do banco de dados e tabela
with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")
