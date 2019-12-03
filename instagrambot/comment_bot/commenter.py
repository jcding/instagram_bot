import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from chatterbot import ChatBot
from instagrambot.comment_bot.chatbot import chatbot



class Commenter:
    def __init__(self, driver):
        self.driver = driver
    
    def write_comment(self):
        time.sleep(2)

        try:
            comment_box_click = self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            # comment_box_elem.send_keys('')
            comment_box_click.click()
        except:
            print("Can't click on comment box")
            pass

        # try:
        comment_box_elem = self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
        print("getting response")
            
            # pic_comment = str(re.sub(r'#.\w*', '', self.get_comments()))
        
        # chatbot = ChatBot('Brandon')
        # chatbot.set_trainer(ListTrainer)

        pic_comment = self.get_comments().replace('#', '')
        pic_comment = pic_comment.replace('\n', ' ')
        pic_comment = str(pic_comment)
        generated_comment = str(chatbot.get_response(pic_comment))
        print("got response")
        print ("User Comment: " + pic_comment)
        print("Bot response: " + generated_comment)

        for letter in generated_comment:
            comment_box_elem.send_keys(letter)
            time.sleep(random.randint(1,7)/30)
        comment_box_elem.send_keys(Keys.RETURN)
        # except:
        #     print("Can't post comment")
        #     pass

        time.sleep(2)
        self.driver.refresh()

    def get_comments(self):
        time.sleep(2)
        comment_block = self.driver.find_element_by_xpath("//div[@class='C4VMK']")
        
        try:
            user_comment = comment_block.find_element_by_xpath("//span[@title='Edited']").text
        except:
            user_comment = comment_block.find_element_by_xpath("//span[not(@*)]").text


        return user_comment
            
            
        # except:
        #     print("cant click comment box")
        #     pass

        





def main():
    print("main")


if __name__ == "__main__":
    main()