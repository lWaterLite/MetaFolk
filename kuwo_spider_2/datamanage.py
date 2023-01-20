# _*_coding : utf-8 _*_
# @Time : 2023/1/19 18:06 
# @Author : 机智的小张
# @File : DataManage 
# @Project : kuwo_spider.py

# 确保mysql启动

import pymysql
import threading


class DataManager():

    # 单例模式，确保每次实例化都调用一个对象。
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DataManager, "_instance"):
            with DataManager._instance_lock:
                DataManager._instance = object.__new__(cls)
                return DataManager._instance

        return DataManager._instance

    def __init__(self):
        # 建立连接
        # python3.8 使用数据库连接的时候前面要有指定的连接名称
        try:
            self.conn = pymysql.connect(host='localhost', user='root', password='111111', database='metafolk', charset='utf8')
            print('数据库连接成功')
            # 建立游标
            self.cursor = self.conn.cursor()

        except pymysql.Error as e:
            print('数据库连接失败:'+str(e))

    def save_data(self, name, artist, lyric):
        # 数据库插入操作

        try:
            insert_song = 'insert into song(song_name) values("{song_name}");'.format(song_name=name)

            self.cursor.execute(insert_song)

            get_song_id ='select song_id from song order by song_id desc limit 1;'

            self.cursor.execute(get_song_id)

            insert_item_song ="insert into item_song(song_ref_id, item_singer) values({song_ref_id}, " \
                           "'{item_singer}');".format(song_ref_id= self.cursor.fetchone()[0], item_singer=artist)

            self.cursor.execute(insert_item_song)

            get_item_id = "select item_id from item_song order by item_id desc limit 1;"

            self.cursor.execute(get_item_id)

            insert_item_lyrics = "insert into item_lyrics(item_ref_id, lyrics) values({item_ref_id}, " \
                                 "'{lyrics}');".format(item_ref_id=self.cursor.fetchone()[0], lyrics=lyric)

            self.cursor.execute(insert_item_lyrics)

            self.conn.commit()

        except Exception as e:
            print('插入数据失败', e)
            self.conn.rollback()  # 回滚

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()