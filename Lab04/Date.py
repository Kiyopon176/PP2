import datetime

'''
Ex 1
'''
x = datetime.datetime.now()

days = []
for i in range(6):
    print((x - datetime.timedelta(days=i)).date())


'''
Ex 2
'''
i = -1
for i in range(3):
    print((x + datetime.timedelta(days=i)).date())

'''
Ex 3
'''

y = x.replace(microsecond=0)

print(y)
      
'''
Ex 4
'''
import time

x = datetime.datetime.now().replace()

time.sleep(4)

y = datetime.datetime.now().replace()
z = y - x
print(z)