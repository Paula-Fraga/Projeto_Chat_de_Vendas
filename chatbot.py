from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Bot():

    def __init__(self):

        self._bot = ChatBot('my_bot', read_only=False,
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "maximum_similarity_threshold": 0.9
                }
            ]
        )

        self._bot_math = ChatBot('math_bot',
            logic_adapters=["chatterbot.logic.MathematicalEvaluation"]
        )
        
        self.trainer = ListTrainer(self._bot)
    
    def get_response_chat_bot(self, message: str):
        resp = ""

        try:
            resp = self._bot_math.get_response(message.lower())
        except:
            resp = self._bot.get_response(message.lower())
        
        return str(resp)

    # Método onde será passado as listas de treinamento do bot.
    def train_bot(self, *messages):
        for i in range(len(messages)):
            self.trainer.train(messages[i])