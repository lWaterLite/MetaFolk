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
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.49'
}
URL = 'https://y.qq.com/n/ryqq/songDetail/003sY8Av2d5wfl'
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
tittle = soup.select('.data__name_txt')[0]
print(tittle.string)
Singer = soup.select('.data__singer_txt')[0]
print(Singer.string)



# Single.songName = tree.xpath('/html/body/div/div/div[2]/div[1]/div/div[1]/h1')
# Single.artists = tree.xpath('/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div')
# Single.artists = tree.xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/a')
# Single.show()

response.close()


