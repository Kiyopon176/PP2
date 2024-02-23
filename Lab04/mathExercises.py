import math

'''
Ex 1
'''
x = math.radians(15)
y = math.degrees(x)
print(x)
print(y)

'''
Ex 2
'''
def TrapezoidArea():
    height = int(input("Height:"))
    base1 = int(input("Base 1:"))
    base2 = int(input("Base 2:"))
    area = (base1 + base2)*(height/2)
    return area
print(TrapezoidArea())
'''
Ex 3
'''
import math

def PolygonArea():
    numSides = int(input("Number Of Sides:"))
    Length = int(input("Length of a side:"))
    p = Length*numSides
    a = Length/(2 * math.tan(math.radians(180/numSides)))
    area = (a * p)/2
    return area
print(PolygonArea())

'''
Ex 4
'''
def ParallelogramArea():
    Base = int(input("Base: "))
    Height = int(input("Height: "))
    return Base * Height

print(ParallelogramArea())