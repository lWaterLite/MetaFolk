
import requests
import re
import json
import pymysql


class Song:

    songName = ''
    artists = ''
    lyric = ''
    mediaUrl = ''

    def show(self):
        print('name = ' + self.songName)
        print('artists = ' + self.artists)
        print('lyric = ' + self.lyric)
        print('mediaUrl = ' + self.mediaUrl)


def getSong(songId):
    """

    :param songId: str
    :return: an instance of the Song class
    """

    theSong = Song()

    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/'
                      '108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    }

    infoUrl = 'https://music.163.com/api/song/detail/?ids=[' + songId + ']'

    infoResponse = requests.get(url=infoUrl, headers=headers).json()

    try:

        info = infoResponse.get('songs')[0]

        theSong.songName = info['name']

        for artist in info['artists']:

            theSong.artists = theSong.artists + artist['name'] + ';'

    except TypeError:

        print(songId + '歌曲信息查询异常，访问过于频繁，请稍后再试')

    lyricResponse = requests.get('https://music.163.com/api/song/lyric?id=' + songId + '&lv=1&kv=1&tv=-1').json()

    lrc = lyricResponse.get('lrc')['lyric']

    theSong.lyric = re.sub('\\[.*?]', '', lrc)

    theSong.mediaUrl = 'http://music.163.com/song/media/outer/url?id=' + songId + '.mp3'

    return theSong


def getSongIdListFromAlbum(albumId):
    """

    :param albumId: str
    :return: a List of songId
    """

    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/'
                      '108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    }

    songIdList = []

    albumUrl = 'http://music.163.com/api/album/' + albumId

    print('第1次查询' + albumId + '专辑信息...')

    albumData = requests.get(url=albumUrl, headers=headers).json()

    count = 1

    while albumData.get('code') != 200:

        count += 1

        print('第' + str(count) + '次查询' + albumId + '专辑信息...')

        albumData = requests.get(url=albumUrl, headers=headers).json()

    albumSongs = albumData.get('album').get('songs')

    for data in albumSongs:

        songIdList.append(data.get('id'))

    return songIdList


def putSongListIntoDB(songList):
    """

    :param songList: a List of instances of class Song
    :return:
    """

    db = pymysql.connect(host='localhost', user='root', password='root', database='metafolk')

    print('数据库连接成功')

    cursor = db.cursor()

    for song in songList:

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


if __name__ == '__main__':

    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/'
                      '108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    }

    searchUrl = 'http://music.163.com/api/search/get/web?s=' \
                '陕北民歌' \
                '&type=10&limit=20'

    searchResponse = requests.get(url=searchUrl).json()

    albums = searchResponse.get('result').get('albums')

    songIdList = []

    for i in range(len(albums)):

        if i < 1:

            albumId = albums[i].get('idStr')

            songIdList.extend(getSongIdListFromAlbum(albumId))

    songList = []

    for songId in songIdList:

        song = getSong(str(songId))

        songList.append(song)

    putSongListIntoDB(songList)

    # with open('songList.json', 'w', encoding='utf-8') as fp:
    #
    #     fp.write('[')
    #
    #     for i in range(len(songList) - 1):
    #
    #         json.dump(obj=songList[i].__dict__, fp=fp, ensure_ascii=False)
    #
    #         fp.write(',')
    #
    #     json.dump(obj=songList[-1].__dict__, fp=fp, ensure_ascii=False)
    #
    #     fp.write(']')
