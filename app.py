from flask import request, Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('my_bot', read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "maximum_similarity_threshold": 0.9
        }
    ]
)

trainer = ListTrainer(bot)
trainer.train([
    "olá",
    "oi, como está?",
    "eu estou bem :)",
    ":)",
    "qual o seu trabalho?",
    "o meu trabalho é te responder",
    "qual é o seu nome?",
    "é chatbot :)!",
    "gosta de vídeo game?",
    "sim, gosto de apex legends",
    "como é o jogo?",
    "fps em primeira pessoa, de battel royale e multiplayer!",
    "não entendi o que vc falou."
])

app = Flask(__name__)


socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('messages') # (<nome do evento do socket>)
def conversationSocket(json):
    data = json
    res_bot = bot.get_response(data['mensagem'].lower())

    print(f"Eu: {data['mensagem']}")
    print(f"Chatbot: {res_bot}")
    
    # Isso vai emitir a mensagem para o evento para o lado do cliente
    socketio.emit('messages', str(res_bot) )

    
if __name__ == "__main__":
    print("Run server!")
    socketio.run(app, debug=False, port=8080)