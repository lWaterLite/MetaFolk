import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Song:
    name = ''
    Singer = ''
    Lyrics = ''

    def show(self):
        print("name : " + self.name)
        print("Singer : " + self.Singer)
        print("Lyrics : " + self.Lyrics)


def getSingle(Id) -> Song:
    try:
        URL = Id
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
        Single.show()
        Page.close()
        return Single
    except NoSuchElementException:
        Error = Song()
        Error.name = 'Error'
        Error.Singer = 'Error'
        Error.Lyrics = 'Error'
        return Error
