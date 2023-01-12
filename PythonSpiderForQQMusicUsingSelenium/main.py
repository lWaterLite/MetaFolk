from getWhole import getWhole
from MusicList import getMusicList

if __name__ == '__main__':
    Id = input("enter the keyword for you spider request")
    ListOfList = getWhole(Id)
    for i in range(1, 4):
        getMusicList(ListOfList[i])


