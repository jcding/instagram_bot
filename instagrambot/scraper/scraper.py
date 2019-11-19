from selenium import webdriver
# from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
# from pandas.io.json import json_normalize
# import pandas as pd, numpy as np
from instagrambot.main import InstagramBot
from instagrambot.model import get_gecko
class Scraper:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=get_gecko())

    
    def scrape(self):
        driver = self.driver
        hashtag='food'

        driver.get('https://www.instagram.com/explore/tags/'+hashtag)
        Pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def main():
    Scrape_Tool = Scraper()
    Scrape_Tool.scrape()
    


if __name__ == "__main__":
    main()