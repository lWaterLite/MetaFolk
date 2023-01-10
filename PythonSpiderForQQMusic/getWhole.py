from Single import getSingle
from Single import Song
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def getWhole(Id) -> list:
    URL = 'https://y.qq.com/n/ryqq/search?w=' + Id + '&t=album&remoteplace=txt.yqq.center'
    MusicList = webdriver.Edge()
    MusicList.get(url=URL)
    input('Please enter an notification to indicate the success of login')
    ListOfList = []
    ListRange = ['1', '2', '3']
    for index in ListRange:
        xPath = '/html/body/div/div/div[3]/div/div/div[2]/ul[2]/li[' + index + ']/h4/span/a'
        ListURL = MusicList.find_element(by=By.XPATH, value=xPath).get_attribute('href')
        ListOfList.append(ListURL)
    MusicList.close()
    return ListOfList
