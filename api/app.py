from flask import Flask 
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = [
    {
        "nome": "Doutor Andre Coelho",
        "email": "andre.coelho@email.com",
        "telefone": "(14) 37382-1245"
    },
    {
        "nome": "Euclides da Cunha",
        "email": "euclides.cunha@email.com",
        "telefone": "(14) 19283-4390"
    },
    {
        "nome": "Joseph Joestar",
        "email": "joseph.joestar@email.com",
        "telefone": "(14) 28374-9283"
    }
]

@app.route("/")
def inicio():
    return "API funcionando!"

@app.route("/usuarios")
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)