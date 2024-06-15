from flask import Flask, jsonify, request

app = Flask(__name__)

# dicionario para registros
pontuacoes = [
    {
        'id': 1,
        'nome': "renata",
        'tempo': 50,
        'pontuacao': 900 
    },
        {
        'id': 2,
        'nome': "marcelo",
        'tempo': 50,
        'pontuacao': 900 
    },
        {
        'id': 3,
        'nome': "carol",
        'tempo': 50,
        'pontuacao': 600 
    }
]

#consultar todos os registros em formato json
@app.route('/pontuacoes',methods=['GET'])
def obter_registros():
    return jsonify(pontuacoes)

#obter registro por id
@app.route('/pontuacoes/<int:id>', methods=['GET'])
def obter_registro(id):
    for registro in pontuacoes:
        if registro.get('id') == id:
            return jsonify(registro)
    return jsonify({'erro': "Nenhum registro encontrado!"})
        
#editar registro por id
@app.route('/pontuacoes/<int:id>', methods=['PUT'])
def editar_registro(id):
    registro_alterado = request.get_json()
    for indice, registro in enumerate(pontuacoes):
        if registro.get('id') == id:
            pontuacoes[indice].update(registro_alterado)
            return jsonify(pontuacoes[indice])
    return jsonify({'erro': "Nenhum registro encontrado!"})
        
# excluir registro por id
@app.route('/pontuacoes/<int:id>', methods=['DELETE'])
def excluir_registro(id):
    for indice, registro in enumerate(pontuacoes):
        if registro.get('id') == id:
            del pontuacoes[indice]
            return jsonify(pontuacoes)
    return jsonify({'erro': "Nenhum registro encontrado!"})

#criar novo registro
@app.route('/pontuacoes', methods=['POST'])
def criar_novo():
    novo_registro = request.get_json()
    pontuacoes.append(novo_registro)
    return jsonify(pontuacoes)

# api que roda na porta 5000, localhost
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)