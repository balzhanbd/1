

class MyShape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled
  def __str__ (self):
    return f"{self.color}({self.is_filled})"
  def getArea(self):
    return 0
class Rectangle(MyShape):
  def __init__ (self, color, is_filled, x_top_left, y_top_left,width, length):
    super().__init__(color,is_filled)
    self.x_top_left = x_top_left
    self.y_top_left = y_top_left
    self.width = width
    self.length = length
  def getArea(self):
    return self.width * self.length
  def __str__ (self):
    return f"{self.color}({self.is_filled}{self.x_top_left}{self.y_top_left}{self.width}{self.length})"
class Circle(MyShape):
  def __init__ (self, color, is_filled, x_center, y_center, radius):
    super().__init__ (color,is_filled)
    self.x_center = x_center
    self.y_center = y_center
    self.radius = radius
  def getArea(self):
    import math
    return math.pi * self.radius**2
  def __str__ (self):
    return f"{self.color}({self.is_filled}{self.x_center}{self.y_center}{self.radius})"
rectangle = Rectangle("blue", True, 0,0,5,4)
print(rectangle)
print(rectangle.getArea())
circle = Circle("red", False, 0,0,3)
print(circle)
print(circle.getArea())
'''shape1 = MyShape("red", True)
print(shape1)
print(shape1.getArea())
'''
