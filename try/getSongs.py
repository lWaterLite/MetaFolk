
import requests
import re
from lxml import etree
import json


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


def getSong(songId):
    """

    :param songId: str
    :return: an instance of the Song class
    """

    theSong = Song()

    infoResponse = requests.get('https://music.163.com/api/song/detail/?ids=[' + songId + ']')

    info = json.loads(infoResponse.text).get('songs')[0]

    theSong.songName = info['name']

    for artist in info['artists']:
        theSong.artists = theSong.artists + artist['name'] + ';'

    lyricResponse = requests.get('https://music.163.com/api/song/lyric?id=' + songId + '&lv=1&kv=1&tv=-1')

    lrc = json.loads(lyricResponse.text).get('lrc')['lyric']

    theSong.lyric = re.sub('\\[.*?]', '', lrc)

    theSong.mediaUrl = 'http://music.163.com/song/media/outer/url?id=' + songId + '.mp3'

    return theSong


if __name__ == '__main__':

    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/'
                      '108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    }

    response = requests.get(url='https://music.163.com/album?id=511958', headers=headers)

    responseText = response.text

    tree = etree.HTML(responseText)

    songUrl = tree.xpath('//ul[@class="f-hide"]/li/a/@href')

    songList = []

    for songId in songUrl:
        if songUrl.index(songId) < 30:
            songId = songId.split('=')[1]
            song = getSong(songId)
            songList.append(song)
        else:
            break

    with open('songList.json', 'w', encoding='utf-8') as fp:
        for song in songList:
            json.dump(obj=song.__dict__, fp=fp, ensure_ascii=False)
