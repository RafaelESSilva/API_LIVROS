from flask import Flask, jsonify,request

main=Flask(__name__)

livros = [
    {
        'id': 1,
        'Nome': 'Codigo limpo',
        'preco': '150'
    },
    {
        'id' : 2,
        'Nome': 'Python',
        'prco': '100',
    },
    {
        'id' : 3,
        'Nome' : 'Logica de Programação',
        'preco' : '59,99'
    },
    {
        'id' : 4,
        'Nome' : 'Se beber não case',
        'preco' : '59,99'
    }
]

# Consultar todos
@main.route('/livros', methods=['GET'])
def obter_livros_():
    return jsonify(livros)
# Consultar por id 

@main.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id :
            return jsonify(livro)

# Editar 
@main.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado=request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id')== id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Incluir novo livro
@main.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro=request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)      
# Excluír
@main.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro_por_id(id):
    for indice,livro in enumerate(livros):
        if livro.get('id')== id:
            del livros[indice]
    return jsonify(livros) 
main.run(port = 5000, host='localhost',debug =True)