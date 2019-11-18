from chatterbot import ChatBot



chatbot = ChatBot('Brandon', trainer='chatterbot.trainers.ListTrainer')
response = chatbot.get_response("Hi there")
print(response)