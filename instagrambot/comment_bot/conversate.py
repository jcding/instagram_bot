from chatterbot import ChatBot
from chatbot import chatbot


while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Bot: ", response)