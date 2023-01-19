# **CloudMusicSpider**
## 免责声明
本应用遵循CC-BY-NC-4.0协议，应用内获取的任何形式的任何文件不得进行任何商业用途，仅作学习交流于讨论用途。使用前请确保此应用合乎您当地法律条令。
## 工程说明
本项目是采用Pycharm创建，数据存于MySQL 8.0。
## 参考文档
Song对象
1. Song对象属性
    + songName : 歌曲名
    + artists : 歌手名
    + lyric : 歌词
    + mediaURL : 音频文件URL    

##使用指南
首先，确保您正确下载了上述软件。然后，在MySQL中运行misc文件夹中的sql文件，在pycharm打开getSongs.py，导入requirements.txt的中的相关依赖包。
最后，运行getSongs.py，数据库中会出现相应歌曲数据。