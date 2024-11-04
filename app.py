from flask import Flask, request, jsonify
from models import db, mission
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Rota para criar uma nova missão
@app.route('/missoes', methods=['POST'])
def criar_missao():
    dados = request.json
    nova_missao = mission(
        nome=dados['nome'],
        data_lancamento=datetime.strptime(dados['data_lancamento'], '%Y-%m-%d').date(),
        destino=dados['destino'],
        estado_missao=dados['estado_missao'],
        tripulacao=dados['tripulacao'],
        carga_util=dados['carga_util'],
        duracao=dados['duracao'],
        custo=dados['custo'],
        detalhes_status=dados['detalhes_status']
    )
    db.session.add(nova_missao)
    db.session.commit()
    return jsonify({"mensagem": "Missão criada com sucesso!"}), 201

# Rota para listar todas as missões
@app.route('/missoes', methods=['GET'])
def obter_missoes():
    missoes = mission.query.order_by(mission.data_lancamento.desc()).all()
    return jsonify([{
        "id": missao.id,
        "nome": missao.nome,
        "data_lancamento": missao.data_lancamento.isoformat(),
        "destino": missao.destino,
        "estado_missao": missao.estado_missao
    } for missao in missoes])

# Rota para obter os detalhes de uma missão específica
@app.route('/missoes/<int:id>', methods=['GET'])
def obter_missao(id):
    missao = mission.query.get_or_404(id)
    return jsonify({
        "id": missao.id,
        "nome": missao.nome,
        "data_lancamento": missao.data_lancamento.isoformat(),
        "destino": missao.destino,
        "estado_missao": missao.estado_missao,
        "tripulacao": missao.tripulacao,
        "carga_util": missao.carga_util,
        "duracao": missao.duracao,
        "custo": missao.custo,
        "detalhes_status": missao.detalhes_status
    })

# Rota para atualizar uma missão existente
@app.route('/missoes/<int:id>', methods=['PUT'])
def atualizar_missao(id):
    dados = request.json
    missao = mission.query.get_or_404(id)
    missao.destino = dados.get('destino', missao.destino)
    missao.estado_missao = dados.get('estado_missao', missao.estado_missao)
    missao.tripulacao = dados.get('tripulacao', missao.tripulacao)
    missao.carga_util = dados.get('carga_util', missao.carga_util)
    missao.duracao = dados.get('duracao', missao.duracao)
    missao.custo = dados.get('custo', missao.custo)
    missao.detalhes_status = dados.get('detalhes_status', missao.detalhes_status)
    db.session.commit()
    return jsonify({"mensagem": "Missão atualizada com sucesso!"})

# Rota para deletar uma missão
@app.route('/missoes/<int:id>', methods=['DELETE'])
def deletar_missao(id):
    missao = mission.query.get_or_404(id)
    db.session.delete(missao)
    db.session.commit()
    return jsonify({"mensagem": "Missão excluída com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
