from chatterbot import ChatBot



chatbot = ChatBot('Brandon', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///comment_bot/db.sqlite3')



# class Bot:
#     def __init__(self):
#         self.chatbot = ChatBot('Brandon')

#     def conversate(self, input):
#         response = self.chatbot.get_response(input)
#         return response
