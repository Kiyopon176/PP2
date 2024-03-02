import math
#Ex 1
s = [2,4,15,1,5,12,6,4,15,1]

a = math.prod(s)
print(a)

#Ex 2

def a(string):
    up = 0
    down = 0
    for i in string:
        if i.isupper():
            up +=1
        else:
            down += 1
    print(up, down)

s = "DwaghGkGiUGiuGiGi"
a(s)

#Ex 3


string = s.lower()

reversed_string = string[::-1]

if string == reversed_string:
    print("Palindrome")
else:
    print("Not palindrome")


#Ex 4
import time

f = 1098409
milliseconds = 1241
seconds = milliseconds/1000
time.sleep(seconds)
b = math.sqrt(f)
print("square of ", f,"was calculated after",milliseconds," milliseconds is", b)

#Ex 5
a = (1,23,1,5,0)
print(all(a))
