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
        
    
    def move(self):
        Xmovement = int(input("input X movement: "))
        Ymovement = int(input("input Y movement: "))
        self.coordinateX += Xmovement
        self.coordinateY += Ymovement
        
    
    def dist(self):
        distance = math.sqrt(self.coordinateX**2 + self.coordinateY**2)
        return distance
    
m1 = Point()
m1.show()
m1.move()
m1.show()
print("Your distance is: ",  m1.dist())
m1.move()
m1.show()


'''
*
*
*
Ex 5
*
*
*
'''

class Account:
    pass

class Bank:
    
    def __init__(self):
        self.owner = input("Enter name of an owner of bank owner:")
        self.balance = 0
    def showBalance(self):
        print( "Now your balance is: ", self.balance, "$")
    def deposit(self):
        depositSum = float(input("Enter amount of your deposit: "))
        self.balance += depositSum
        self.showBalance()

    def withdraw(self):
        withdrawAmount = float(input("Enter amount of withdrawal: "))
        if(withdrawAmount <= self.balance and withdrawAmount > 0):
            self.balance -= withdrawAmount
            self.showBalance()
        else:
            print("You cannot wihtdraw your money.")


m1 = Bank()
m1.deposit()
m1.withdraw()
m2 = Bank()
m2.deposit()
m2.withdraw()
m1.showBalance()
m2.showBalance()
'''
*
*
*
Ex 6
*
*
*
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))


print("Prime numbers in the list:", prime_numbers)
