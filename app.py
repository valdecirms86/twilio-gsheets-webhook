
from flask import Flask, request
from utils import append_to_sheet
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.form.get("Body")
    if msg:
        dados = [x.strip() for x in msg.split(",")]
        if len(dados) == 4:
            categoria, valor, descricao, data = dados
            append_to_sheet(categoria, valor, descricao, data)
            return "Adicionado com sucesso!"
        else:
            return "Formato inválido. Use: categoria, valor, descrição, data"
    return "Nenhuma mensagem recebida"
