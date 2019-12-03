from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import getpass
from instagrambot.model import get_gecko

from instagrambot.commenter import Commenter
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        geckodir = get_gecko()
        self.driver = webdriver.Firefox(executable_path=geckodir)

    def closeBrowser(self):
        self.driver.close()

    # <a href="/accounts/login/?source=auth_switcher">Log in</a>

    # "//a[@href='/accounts/login/?source=auth_switcher']"

    # username
    # "//input[@name='username']"

    # password
    # "//input[@name='password']"

    # login button
    # "//button[@type='submit']"

    def login(self):
        print("Logging in....")
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)

        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)

        time.sleep(4)
        # if we find the "Turn on Notifications" box
        try:
            notification_elem = driver.find_element_by_xpath("//div[@role='dialog']")
            print ("Found notification box")
            not_now = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
            not_now.click()
            print("Turned off Notifications")
        except:
            print ("No \"Turn on Notifications\" box")
        time.sleep(2)
        print("Success")

    
    def like_person_post(self, person_username):
        driver = self.driver
        # go to home page first
        driver.get("https://www.instagram.com/")
        search_box = driver.find_element_by_xpath("//div[@class='eyXLr wUAXj ']")
        search_box.click()
        
        enter_name = driver.find_element_by_xpath("//input[@placeholder='Search']")
        enter_name.send_keys(person_username)
        time.sleep(1)
        enter_name.send_keys(Keys.RETURN)
        enter_name.send_keys(Keys.RETURN)
        time.sleep(2)

        for i in range (1,10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        # pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = []
        pattern = re.compile("https://www.instagram.com/p/*")

        

        for elem in hrefs:
            url = elem.get_attribute('href')
            if (pattern.match(url)):
                pic_hrefs.append(url)

        for pic_url in pic_hrefs:
            # print(pic_url)
            driver.get(pic_url)
            time.sleep(2)
            
            # we havent liked the picture yet
            try:
                driver.find_element_by_xpath("//span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
                like_button = driver.find_element_by_xpath("//button[@class='dCJp8 afkep']")
                like_button.click()
                print ("Liked image: "+ pic_url)
                # time.sleep(19)
            except:
                print("Already liked picture: " + pic_url)

    def comment(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        CommenterBot = Commenter(driver)
        CommenterBot.write_comment()


def main():
    # username = input("What is your Instagram username? ")
    # type(username)
    print("Username: jsondingding")
    password = getpass.getpass("What is your Instagram password? ")

    IGBot = InstagramBot("jsondingding", password)
    IGBot.login()

    

    while True:
        print("What would you like to do today?")
        print("Options:")
        print("\t'like-user-pics': like all pictures from a specific user")
        print("\t'comment': use machine learning to automatically chat with users")
        print("\t'exit': exit the program")
        print()
        option = input("Enter: ")
        type(option)

        if(option == "like-user-pics"):
            like_user = input("Which users pictures do you want to like: ")
            IGBot.like_person_post(like_user)
            print("Success")
            print()
        elif(option == "comment"):
            IGBot.comment("https://www.instagram.com/p/B5mG1n0lnIM/")
        elif(option == "exit"):
            break
        else:
            print("Sorry, not a valid option")

        
    

        


if __name__ == "__main__":
    main()