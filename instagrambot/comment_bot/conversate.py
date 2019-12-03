from chatterbot import ChatBot



bot = ChatBot('Brandon')
while True:
    request = input("You: ")
    response = bot.get_response(request)
    print("Bot: ", response)

# print(bot.get_response("Rigatoni �🍝 via @jakecohen . . . . noodleworship tastethisnext pasta rigatoni buzzfeast yum noodles 9gag lunch zagat cheatmeal cheatday dinner food foodiegram instafood yummy complex eeeeeats tasty foodie eat foodpics foo hotography hungry lovefood"))