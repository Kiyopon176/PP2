'''
Ex 1
'''

def SquareNums(n):
    for i in range(n):
        yield(i*i)

a = SquareNums(6)

for i in a:
    print(i)

'''
Ex 2
'''
def EvenNums(N):
    for i in range(N):
        if i % 2 == 0:
            yield i

n = int(input())
a = EvenNums(n)
s = ""
for i in a:
    s += str(i) + ","

print(s)


'''
Ex 3
'''
def divisible_by_3_and_4(N):
    for i in range(N):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
a = divisible_by_3_and_4(n)
s = ""
for i in a:
    s += str(i) + ","

print(s)

'''
Ex 4
'''

def SquareNums_A_To_B(a,b):
    for i in range(a,b+1):
        yield(i*i)

a = SquareNums_A_To_B(2,50)

for i in a:
    print(i)

'''Ex 5'''

def Declining(n):
    while n >=0:
        print(n)
        n -= 1

Declining(10)