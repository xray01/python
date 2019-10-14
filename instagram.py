from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
class InstagramBot:
    def __init__(self, username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
    def CloseBrowser(self):
        self.driver.close()
    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(5)
        login_button = driver.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[2]/p/a')
        login_button.click()
        time.sleep(5)
        username_box = driver.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        username_box.clear()
        username_box.send_keys(self.username)
        password_box = driver.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.get('https://instagram.com/{}' .format(self.username))
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(5)
        pic_hrefs = []
        for i in range(1,2):
            try:
                driver.execute_script("window.scrollTo(0 , document.body.scrollHeigh)")
                time.sleep(2)
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p' in elem.get_attribute('href')]
            except Exception:
                continue
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(5)
            try:
                time.sleep(random.randint(1,2))
                driver.find_elements_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')
            except Exception: 
                time.sleep(5)
username = 'da.nial3625'
password = 'danial_1382'
ig = InstagramBot(username,password)
ig.Login()
hashtag = ["animals"]
while True:
    try:
        tag = random.choice(hashtag)
        ig.like_photo(tag)
    except Exception:
        ig.CloseBrowser()
        time.sleep(5)
        ig = InstagramBot(username, password)
        ig.Login()