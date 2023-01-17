import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
class Song:
    name = ''
    Singer = ''
    lyrics = ''
    MediaUrl = ''
    Songmid = ''


    def show(self):
        print("name : " + self.name)
        print("Singer : " + self.Singer)
        print("Lyrics : " + self.Lyrics)
        print("mediaUrl:"+self.MediaUrl)


URL = 'https://y.qq.com/n/ryqq/songDetail/004JlZmv4MmD14'
index = URL.index('songDetail/')
id = ''
for i in range(index+11, len(URL)):
    id = id+URL[i]
print(id)
Page = webdriver.Edge()
Page.get(url=URL)
time.sleep(5)
a = Page.find_element(
    By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a')
Page.execute_script("arguments[0].click();", a)
Single = Song()
Single.name = Page.find_element(
    by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div[1]/h1').text
Single.Singer = Page.find_element(
    by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div[2]/a').text
Lyrics = Page.find_element(
    by=By.XPATH, value='/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div')
Single.Lyrics = Lyrics.text
# Single.show()
options = webdriver.EdgeOptions()
mobileEmulation = {"deviceName": "iPhone 6"}
options.add_experimental_option("mobileEmulation", mobileEmulation)
Mobile = webdriver.Edge(options=options)
Mobile.get(url='https://i.y.qq.com/v8/playsong.html?songmid=004JlZmv4MmD14')
time.sleep(5)
MediaUrl = Mobile.find_element(by=By.XPATH, value='//audio')
Single.MediaUrl = MediaUrl.get_attribute('src')
Single.show()
Mobile.close()
Page.close()
