from flask import Flask,jsonify,request
from flask_cors import CORS
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv

#Leituura da chave de API
load_dotenv()

app = Flask (__name__)

CORS(app)

agente = Agent (
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um agente virtual do Hotel do minecraft que sempre comeca a mensagem com criatividade"
    "Você responde de uma forma clara e humorada, informações sobre quartos, serviços, reservas e preços"
    "Quarto Standard ($500), Quarto Delux ($700), Quarto Suite presidencial ($1000)",
    markdown=True
)

@app.route("/chat",methods=['GET'])
def testar():
    return jsonify({"mensagem":"API funcionando"})


@app.route("/chat",methods=['POST'])
def pergunta():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta = agente.run(pergunta)
    return jsonify ({"resposta":resposta.content})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)