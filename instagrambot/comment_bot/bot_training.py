from chatterbot import ChatBot
from chatbot import chatbot

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pickle

from instagrambot.scraper.scraper import Scraper


# chatbot = ChatBot('Brandon', trainer='chatterbot.trainers.ListTrainer')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

trainer = ListTrainer(chatbot)
f = open("./InstagramComments_.p", "rb")
comments = pickle.load(f)
f.close()


My_scraper = Scraper()

my_data = My_scraper.scrape()

for data in my_data:
    print(data)
    trainer.train(data)

for convo in comments[:10000]:
    trainer.train(convo)