import json
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pymysql

MusicList = []
check = dict()


class Song:
    Name = ''
    Singer = ''
    lyrics = ''
    MediaUrl = ''
    SongMId = ''

    def show(self):
        print("name : " + self.Name)
        print("Singer : " + self.Singer)
        print("Lyrics : " + self.lyrics)
        print("mediaUrl:" + self.MediaUrl)


def store():
    with open('songList.json', 'w', encoding='utf-8') as fp:
        for song in MusicList:
            db = pymysql.connect(host='localhost', user='root', password='', database='metafolk')
            cursor = db.cursor()
            insert_Song = "insert into song(song_name) values('{song_name}');".format(song_name=song.songName)

            cursor.execute(insert_Song)

            get_song_id = "select song_id from song order by song_id desc limit 1;"

            cursor.execute(get_song_id)

            insert_item_song = "insert into item_song(song_ref_id, item_singer) values({song_ref_id}, " \
                               "'{item_singer}');".format(
                song_ref_id=cursor.fetchone()[0], item_singer=song.artists)

            cursor.execute(insert_item_song)

            get_item_id = "select item_id from item_song order by item_id desc limit 1;"

            cursor.execute(get_item_id)

            insert_item_lyrics = "insert into item_lyrics(item_ref_id, lyrics) values({item_ref_id}, " \
                                 "'{lyrics}');".format(
                item_ref_id=cursor.fetchone()[0], lyrics=song.lyric)

            cursor.execute(insert_item_lyrics)

        db.commit()

        cursor.close()

        db.close()
        json.dump(obj=song.__dict__, fp=fp, ensure_ascii=False)


def getSingle(Id) -> Song:
    try:
        URL = Id
        Page = webdriver.Edge()
        Page.get(url=URL)
        Single = Song()
        time.sleep(3)
        a = Page.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a')
        Page.execute_script("arguments[0].click();", a)
        Page.implicitly_wait(5)
        Single.Name = Page.find_element(
            by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div[1]/h1').text
        Single.Singer = Page.find_element(
            by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div[2]/a').text
        Lyrics = Page.find_element(
            by=By.XPATH, value='/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div')
        Single.lyrics = Lyrics.text
        Page.close()
        index = URL.index('songDetail/')
        ID = ''
        for index in range(index + 11, len(URL)):
            ID = ID + URL[index]
        Single.SongMId = ID
        MobileUrl = 'https://i.y.qq.com/v8/playsong.html?songmid={}'.format(ID)
        options = webdriver.EdgeOptions()
        mobileEmulation = {"deviceName": "iPhone 6"}
        options.add_experimental_option("mobileEmulation", mobileEmulation)
        Mobile = webdriver.Edge(options=options)
        Mobile.get(url=MobileUrl)
        Mobile.implicitly_wait(5)
        MediaUrl = Mobile.find_element(by=By.XPATH, value='/html/body/audio')
        Single.MediaUrl = MediaUrl.get_attribute('src')
        if check.get(Single.Name + Single.Singer, False):
            pass
        else:
            check[Single.Name + Single.Singer] = True
            MusicList.append(Single)
            Mobile.close()
            Single.show()
        return Single
    except NoSuchElementException:
        Error = Song()
        Error.Name = 'Error'
        Error.Singer = 'Error'
        Error.lyrics = 'Error'
        Error.SongMId = 'Error'
        Error.MediaUrl = 'Error'
        return Error


def getMusicList(id) -> list:
    URL = id
    MusicListPage = webdriver.Edge()
    MusicListPage.get(url=URL)
    time.sleep(5)
    SingleList = []
    ListRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    try:
        for index in ListRange:
            xPath = '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/ul[2]/li[' + index + ']/div/div[2]/span/a'
            SingleURL = MusicListPage.find_element(by=By.XPATH, value=xPath).get_attribute('href')
            Single = getSingle(SingleURL)
            SingleList.append(Single)
    except NoSuchElementException:
        pass
    MusicListPage.close()
    return SingleList


def getWhole(Id) -> list:
    URL = 'https://y.qq.com/n/ryqq/search?w=' + Id + '&t=playlist&remoteplace=txt.yqq.playlist'
    MusicListPage = webdriver.Edge()
    MusicListPage.get(url=URL)
    input('Please enter an notification to indicate the success of login')
    ListOfList = []
    ListRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for index in ListRange:
        try:
            xPath = '/html/body/div/div/div[3]/div/div/div[2]/ul[2]/li[' + index + ']/h4/span/a'
            ListURL = MusicListPage.find_element(by=By.XPATH, value=xPath).get_attribute('href')
            ListOfList.append(ListURL)
        except NoSuchElementException:
            pass
    MusicListPage.close()
    return ListOfList


if __name__ == '__main__':
    Id = input("enter the keyword for you spider request")
    ListOfList = getWhole(Id)
    for i in range(1, 4):
        getMusicList(ListOfList[i])
    store()
