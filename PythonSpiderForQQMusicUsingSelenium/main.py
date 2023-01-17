import json
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

MusicList = []
check = dict()


class Song:
    name = ''
    Singer = ''
    lyrics = ''
    MediaUrl = ''
    SongMId = ''

    def show(self):
        print("name : " + self.name)
        print("Singer : " + self.Singer)
        print("Lyrics : " + self.Lyrics)
        print("mediaUrl:" + self.MediaUrl)


def store():
    with open('songList.json', 'w', encoding='utf-8') as fp:
        for song in MusicList:
            json.dump(obj=song.__dict__, fp=fp, ensure_ascii=False)


def getSingle(Id) -> Song:
    try:
        URL = Id
        Page = webdriver.Edge()
        Page.get(url=URL)
        Single = Song()
        Page.implicitly_wait(5)
        a = Page.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a')
        Page.execute_script("arguments[0].click();", a)
        time.sleep(1)
        Single.name = Page.find_element(
            by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div[1]/h1').text
        Single.Singer = Page.find_element(
            by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div[2]/a').text
        Lyrics = Page.find_element(
            by=By.XPATH, value='/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div')
        Single.Lyrics = Lyrics.text
        Page.close()
        index = URL.index('songDetail/')
        Id = ''
        for i in range(index + 11, len(URL)):
            Id = Id + URL[i]
        Single.SongMId = Id
        MobileUrl = 'https://i.y.qq.com/v8/playsong.html?songmid={}'.format(Id)
        options = webdriver.EdgeOptions()
        mobileEmulation = {"deviceName": "iPhone 6"}
        options.add_experimental_option("mobileEmulation", mobileEmulation)
        Mobile = webdriver.Edge(options=options)
        Mobile.get(url=MobileUrl)
        Mobile.implicitly_wait(5)
        MediaUrl = Mobile.find_element(by=By.XPATH, value='/html/body/audio')
        Single.MediaUrl = MediaUrl.get_attribute('src')
        if check.get(Single.name + Single.Singer, False):
            pass
        else:
            check[Single.name + Single.Singer] = True
            MusicList.append(Single)
            Mobile.close()
            Single.show()
        return Single
    except NoSuchElementException:
        Error = Song()
        Error.name = 'Error'
        Error.Singer = 'Error'
        Error.Lyrics = 'Error'
        Error.SongMId = 'Error'
        Error.MediaUrl = 'Error'
        return Error


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


def getWhole(Id) -> list:
    URL = 'https://y.qq.com/n/ryqq/search?w=' + Id + '&t=playlist&remoteplace=txt.yqq.playlist'
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


if __name__ == '__main__':
    Id = input("enter the keyword for you spider request")
    ListOfList = getWhole(Id)
    for i in range(1, 4):
        getMusicList(ListOfList[i])
    store()
