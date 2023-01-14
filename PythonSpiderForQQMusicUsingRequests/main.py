from lxml import etree
from bs4 import BeautifulSoup
import requests

class Song:
    songName = ''
    artists = ''
    lyric = ''
    mediaUrl = ''

    def show(self):
        print('name = ' + self.songName)
        print('artists = ' + self.artists)
        print('lyric = ' + self.lyric)
        print('url = ' + self.url)


headers = {
'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
URL = 'https://i.y.qq.com/v8/playsong.html?ADTAG=ryqq.songDetail&songmid={}&songid=0&songtype=0#webchat_redirect'.format('003sY8Av2d5wfl')
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
print(soup.find('audio'))



#soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
#Single = Song()

# Single.songName = tree.xpath('/html/body/div/div/div[2]/div[1]/div/div[1]/h1')
# Single.artists = tree.xpath('/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div')
# Single.artists = tree.xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/a')
# Single.show()

response.close()


