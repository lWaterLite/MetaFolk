# **CloudMusicSpider**
## 免责声明
本应用遵循CC-BY-NC-4.0协议，应用内获取的任何形式的任何文件不得进行任何商业用途，仅作学习交流于讨论用途。使用前请确保此应用合乎您当地法律条令。
## 工程说明
本项目是采用Pycharm创建，依赖包通过pip导出为requirements.txt。
## 参考文档
Song对象
1. Song对象属性
    + songName : 歌曲名
    + artists : 歌手名
    + lyric : 歌词
    + mediaURL : 音频文件URL    

2. 获取Song对象方法
    + getSong(songId)
        > songId: 歌曲的Id

        返回值为Song对象
## 使用指南
通过pycharm打开getSongs.py，通过pip导入requirements.txt的中的相关依赖包
运行getSongs.py，同级目录下会生成一个json文件，其中是Songs的信息。