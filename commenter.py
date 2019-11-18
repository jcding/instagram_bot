import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Commenter:
    def __init__(self, driver):
        self.driver = driver
    
    def write_comment(self, text):
        # try:
        #     comment_button = lambda: self.driver.find_element_by_xpath("//span[@aria-label='Comment']")
        #     comment_button.click()
        #     print("Clicked comment button")
        # except:
        #     print("Can't click comment button")
        #     pass

        try:
            comment_box_click = self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            # comment_box_elem.send_keys('')
            comment_box_click.click()
        except:
            print("Can't click on comment box")
            pass

        try:    
            comment_box_elem = self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")

            for letter in text:
                comment_box_elem.send_keys(letter)
                time.sleep(random.randint(1,7)/30)
            comment_box_elem.send_keys(Keys.RETURN)
        except:
            print("Can't post comment")
            pass

        driver.refresh()
            
            
            
        # except:
        #     print("cant click comment box")
        #     pass

        





def main():
    print("main")


if __name__ == "__main__":
    main()