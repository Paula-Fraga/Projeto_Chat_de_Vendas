from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api

from chatbot import Bot
from train_list import TrainList

# Classes controladoras
from controllers.teste_socket import TesteSocket

app = Flask(__name__)
api = Api(app)

# Meus controladores
api.add_resource(TesteSocket, '/teste')

socketio = SocketIO(app, cors_allowed_origins="*")

bot = Bot()

@socketio.on('messages') # (<nome do evento do socket>)
def conversation_chatbot_socket(json):
    data = json
    res_bot = bot.get_response_chat_bot(data['mensagem'].lower())

    print(f"Eu: {data['mensagem']}")
    print(f"Chatbot: {res_bot}")
    
    # Isso vai emitir a mensagem para o evento para o lado do cliente
    socketio.emit('messages', str(res_bot))

    
if __name__ == "__main__":
    port = 8080
    print(f"Run server in port {port}")
    bot.train_bot(TrainList.first_list_conversation("R2-D2"))
    socketio.run(app, debug=False, port=port)