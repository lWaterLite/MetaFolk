# **SpiderForQQMusic**
## 免责声明
应用内获取的任何形式的任何文件不得进行任何商业用途，仅作学习交流于讨论用途。使用前请确保此应用合乎您当地法律条令。
## 工程说明
本项目是采用Pycharm创建，基于Edge浏览器的爬虫程序，使用本程序应安装Edge浏览器，并安装相应的EdgeDriver,依赖包通过pip导出为requirements.txt。
## 参考文档
Song对象
1. Song对象属性
    + Name : 歌曲名
    + Singer : 歌手名
    + lyrics : 歌词 

2. 获取单曲方法
    + getSingle(songId)
        > songId: 歌曲的Id,可通过歌曲URL获得

        返回值为Song对象
3. 获取歌单方法   
    + getMusicList(Id)
    > Id 歌单的Id   
   
    返回值为list对象
4. 获取整个搜索页面的方法
    + getWhole(Id)
    > Id为整个搜索页面的Id（搜索的关键词）

    返回值为list对象
## 食用方法
运行main.py,出现 'enter the keyword for you spider request'需要输入你想要采集的信息的关键字    
本程序需要手动登录 手动登录结束后，出现'Please enter an notification to indicate the success of login'   
表示需要输入一个提示来表明成功登录，随便输入都行，然后程序就会自动运行，获取歌曲的名字，   
歌手，歌词，全部显示在console中,程序会有些慢，我设置的time.sleep(5)
萌新第一次写爬虫,只会用selenium.......不多说了，学requests去了   
记得填完整密码
    
