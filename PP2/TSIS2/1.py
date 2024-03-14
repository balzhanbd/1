class Qube:
    def __init__ (self, length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def getVolume(self):
        return 0
class Square(Qube):
    def __init__ (self, length, width, height):
        self.length = length
        self.width = width
        self.height
    def getVolume(self):
        return self.length*self.height*self.width