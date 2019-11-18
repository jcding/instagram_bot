from chatterbot import ChatBot



chatbot = ChatBot('Brandon')


while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Bot: ", response)