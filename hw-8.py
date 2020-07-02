class Worm:
    def __init__(self, initialPosition):
        self.__direction=1
        self.__Position=0
        if(type(initialPosition)==int or type(initialPosition)==float):
            self.__Position=initialPosition
            print("初始化位置成功了")
        else:
            print("初始化位置违法了")
    def turn(self):
        print("方向改变了")
        self.__direction=self.__direction*-1
    def move(self):
        print("单位移动了")
        self.__Position+=self.__direction
    def getPosition(self):
        print("当前位置：",self.__Position)

worm0=Worm('abc')
worm1=Worm(0)
worm1.getPosition()
worm1.move()
worm1.getPosition()
worm1.move()
worm1.getPosition()
worm1.turn()
worm1.getPosition()
worm1.move()
worm1.getPosition()