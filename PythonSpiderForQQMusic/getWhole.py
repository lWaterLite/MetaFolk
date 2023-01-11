
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


def getWhole(Id) -> list:
    URL = 'https://y.qq.com/n/ryqq/search?w='+Id+'&t=playlist&remoteplace=txt.yqq.playlist'
    MusicList = webdriver.Edge()
    MusicList.get(url=URL)
    input('Please enter an notification to indicate the success of login')
    ListOfList = []
    ListRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for index in ListRange:
        try:
            xPath = '/html/body/div/div/div[3]/div/div/div[2]/ul[2]/li[' + index + ']/h4/span/a'
            ListURL = MusicList.find_element(by=By.XPATH, value=xPath).get_attribute('href')
            ListOfList.append(ListURL)
        except NoSuchElementException:
            pass
    MusicList.close()
    return ListOfList
