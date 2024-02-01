#Python Boolean

#Ex 1
print(10 > 9)
#True

#Ex 2
print(10 == 9)
#False

#Ex 3
print(10 < 9)
#False

#Ex 4
print(bool("abc"))
#True

#Ex 5
print(bool(0))
#False


#PYTHON OPERATIONS

#Ex 1
print(10*5)

#Ex 2
print(10/5)

#Ex 3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Ex 4
if 5 != 10:
  print("5 and 10 is not equal")

#Ex 5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#PYTHON LISTS

#Ex 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Ex 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Ex 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Ex 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Ex 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Ex 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Ex 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Ex 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#PYTHON TUPLES

#Ex 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Ex 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Ex 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Ex 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#PYTHON SETS

#Ex 1

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Ex 2
fruits = ("apple", "banana", "cherry")
fruits.add("orange")

#Ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#PYTHON DICTIONARIES
#Ex 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Ex 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Ex 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Ex 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Ex 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#PYTHON IF...ELSE

#Ex 1
a = 50
b = 10
if a>b:
  print("Hello World")

#Ex 2
a = 50
b = 10
if a!=b:
  print("Hello World")

#Ex 3
a = 50
b = 10
if a==b:
  print("Yes")
else:
    print("No")

#Ex 4
a = 50
b = 10
if a==b:
  print("1")
elif a > b:
    print("2")
else:
    print("3")

#Ex 5
if a == b and c == d:
  print("Hello")

#Ex 6
if a == b or c == d:
  print("Hello")

#Ex 7
if 5 > 2:
    print("Yes")

#Ex 8
a = 2
b = 5
print("YES") if a == b else print("NO")

#Ex 9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#PYTHON WHILE LOOPS

#Ex 1
i = 1
while i < 6:
    print(i)
    i += 1

#Ex 2
i = 1
while i < 6:
  if i == 3:
    break

    i += 1

#Ex 3
i = 1
while i < 6:
  if i == 3:
    continue

    i += 1

#Ex 4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#PYTHON FOR LOOPS

#Ex 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Ex 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Ex 3
for x in range(6):
    print(x)

#Ex 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
