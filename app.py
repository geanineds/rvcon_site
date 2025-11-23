from flask import Flask, render_template, request, jsonify
from chatbot import responder

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    user_msg = request.json.get("message", "")
    resposta = responder(user_msg)
    return jsonify({"answer": resposta})


@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    servico = request.form.get("servico")
    descricao = request.form.get("descricao")

    mensagem = f"Olá! Meu nome é {nome}. Telefone: {telefone}. Serviço desejado: {servico}. Descrição: {descricao}"
    link = f"https://wa.me/5541991194424?text={mensagem.replace(' ', '%20')}"

    return jsonify({"link": link})


if __name__ == "__main__":
    app.run(debug=True)
