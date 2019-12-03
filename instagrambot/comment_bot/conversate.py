from chatterbot import ChatBot


brandon = ChatBot('Brandon')

while True:
    request = input("You: ")
    response = brandon.get_response(request)
    print("Bot: ", response)