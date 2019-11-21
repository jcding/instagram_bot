from selenium import webdriver
# from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
# from pandas.io.json import json_normalize
# import pandas as pd, numpy as np
from selenium.webdriver.common.keys import Keys
from instagrambot.main import InstagramBot
from instagrambot.model import get_gecko

from instagram_private_api import Client, ClientCompatPatch

class Scraper:
    def __init__(self):
        self.username = "jsondingding"
        self.password = "test1234!"

    
    def scrape(self):
        api = Client(self.username, self.password)
        results = api.feed_timeline()

        comments_vector = []
        #print(results)

        items = [item for item in results.get('feed_items', []) if item.get('media_or_ad')]
        for item in items:
            # Manually patch the entity to match the public api as closely as possible, optional
            # To automatically patch entities, initialise the Client with auto_patch=True
            ClientCompatPatch.media(item['media_or_ad'])

            if('ad_metadata' not in  item['media_or_ad'].keys()):

                # print(item['media_or_ad']['code'])
                # print("#####################")
                

                # print(item['media_or_ad']['caption']['text'])
                

                media_id = item['media_or_ad']['caption']['media_id']

                comments = api.media_comments(media_id)
            
                # print("#####################")
                # print(comments)
                for comment in comments['comments']:
                    comment_vector = []
                    comment_vector.append(item['media_or_ad']['caption']['text'])
                    comment_vector.append(comment['text'])
                    # print(comment['text'])
                    comments_vector.append(comment_vector)

        
        return comments_vector



def main():
    Scrape_Tool = Scraper()
    # Scrape_Tool.login()
    Scrape_Tool.scrape()
    


if __name__ == "__main__":
    main()