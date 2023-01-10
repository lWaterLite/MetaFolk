from selenium.common import NoSuchElementException

from Single import getSingle
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def getMusicList(Id) -> list:
    URL = Id
    MusicList = webdriver.Edge()
    MusicList.get(url=URL)
    time.sleep(5)
    SingleList = []
    ListRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    try:
        for index in ListRange:
            xPath = '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/ul[2]/li[' + index + ']/div/div[2]/span/a'
            SingleURL = MusicList.find_element(by=By.XPATH, value=xPath).get_attribute('href')
            Single = getSingle(SingleURL)
            SingleList.append(Single)
    except NoSuchElementException:
        pass
    MusicList.close()
    return SingleList


