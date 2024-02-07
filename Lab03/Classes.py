import math
'''
*
*
*
Ex 1
*
*
*
'''

class MyClass:
    def __init__(self, text):
        self.text = text
    
    def GetString(self):
        self.text = input("Input something: ")
        return
    
    def PrintString(self):
        print("That is what you wrote: '"+ self.text+ "'")
        return

m1 = MyClass("")


m1.GetString()
m1.PrintString()

'''
*
*
*
Ex 2
*
*
*
'''
class Shape:
    def __init__(self):
        self.area = 0
    
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def calculate_area(self):
        self.area = self.length * self.length
        return self.area

m1 = Square(4)
print(m1.calculate_area()) 

'''
*
*
*
Ex 3
*
*
*
'''


class Rectangular(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def calculate_area(self):
        self.area = self.length * self.width
        
        return self.area
    

m2 = Rectangular(5, 3)
print(m2.calculate_area())
    

m2 = Rectangular(5, 3)
print(m2.calculate_area())

'''
*
*
*
Ex 4
*
*
*
'''

class Point:
    def __init__(self):
        self.coordinateX = 0
        self.coordinateY = 0
    def show(self):
        print(self.coordinateX, "," , self.coordinateY )
        return
    def move(self):
        Xmovement = int(input("input X movement: "))
        Ymovement = int(input("input Y movement: "))
        self.coordinateX += Xmovement
        self.coordinateY += Ymovement
        return
    def dist(self):
        distance += math.sqrt(self.coordinateX**2 + self.coordinateY**2)
        return distance
    
m1 = Point()
m1.show()
m1.move()
m1.show()
print("Your distance is: ",  m1.dist())
m1.move()
m1.show()
