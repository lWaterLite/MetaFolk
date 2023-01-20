# _*_coding : utf-8 _*_
# @Time : 2023/1/14 20:40 
# @Author : 机智的小张
# @File : 酷我test4 
# @Project : pythonProject

import requests
import json
from datamanage import DataManager


def kuwo_spider():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1673560008; _ga=GA1.2.1201856314.1673560009; _gid=GA1.2.1781482575.1673560009; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1673707895; _gat=1; kw_token=CP2LLS01W5P',
        'csrf': 'CP2LLS01W5P',
        'Host': 'www.kuwo.cn',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E9%99%95%E5%8C%97%E6%B0%91%E6%AD%8C',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    page = int(input('请输入要爬取的页码:'))
    url_music_info = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%E9%99%95%E5%8C%97%E6%B0%91%E6%AD%8C&pn={page}&rn=30&httpsStatus=1&reqId=11f4b0f0-941b-11ed-ac6c-1d4a48fa07c2'
    url_mp3 = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=mp3&httpsStatus=1&reqId=7ac6cc31-941b-11ed-ac6c-1d4a48fa07c2'

    res = requests.get(url=url_music_info, headers=headers)
    music_info_data = dict(json.loads(res.text))
    music_info_list = music_info_data['data']['list']

    for music_info in music_info_list:

        name = music_info['name']       # 歌曲名(string)
        rid = music_info['rid']         # song_ref_rid
        artist = music_info['artist']   # item_singer

        # 录歌词

        ly = music_lyric(rid, name, artist)

        print('开始导数据到数据库：')
        db.save_data(name, artist, ly)

        '''
        # 下载mp3

        with open(f'{name}.mp3', 'wb') as f:
            playUrl = url = url_mp3.format(rid)
            mp3 = json.loads(requests.get(playUrl).text)['data']['url']
            f.write(requests.get(mp3).content)
            print('爬取音频成功')
        '''

def music_lyric(rid, name, artist):
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT10.0;Win64;x64)'
    }

    url_music_lyric = 'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={}'.format(rid)
    res = requests.get(url=url_music_lyric, headers=headers)
    music_info_data = dict(json.loads(res.text))
    music_info_lrclist = music_info_data['data']['lrclist']

    # print(music_info_lrclist)

    sum_lyric = ''

    if music_info_lrclist:  # music_info_lrclist 存在None（即没有歌词) 会引起循环语句错误

        for lrclist in music_info_lrclist:

            lyric = lrclist['lineLyric']
            sum_lyric = sum_lyric + lyric + ' '
            # print(sum_lyric)

        ''' 写歌词入txt文件
        
            with open(f'{name}-{artist}.text', 'a') as f:
                f.write(lyric)
                f.write('\r\n')
        '''
        print(name, artist, '爬取歌词成功!')


    else:
        print(name, artist, '该歌没有歌词')
        with open(f'{name}-{artist}.text', 'a') as f:
            f.write('没有歌词')

    return sum_lyric



if __name__ == '__main__':
    print('爬取页面为:', 'http://www.kuwo.cn/search/list?key=%E9%99%95%E5%8C%97%E6%B0%91%E6%AD%8C')
    db = DataManager()
    kuwo_spider()
