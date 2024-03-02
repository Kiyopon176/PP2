import os

path = os.getcwd()

print(os.listdir(path))

#Ex 2
p = r"C:\Users\NEXTGENPC\Desktop\PP2\Lab04\Date.py"
print(os.path.isfile(p))
print(os.path.isabs(p))
print(os.path.isdir(p))

#Ex 3
if(os.path.isdir(p)):
    print(os.path.basename(path))

#Ex 4
with open("row.txt", "r", encoding="utf-8") as file:
    filetxt = file.read().splitlines()
print(len(filetxt))

#Ex 5
list = [12,5,4,14,1,35,51,15,3,5,135]
with open("file.txt", "w") as file:
    file.write(str(list))

#Ex 6
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabet:
    name = i +".txt"
    with open(name, "w") as file:
        file.write(name)
#Ex 7
file1 = open("A.txt", "r")
file2 = open("B.txt", "w")
str = file1.read()
file2.write(str)
file1.close()
file2.close()
#Ex 8
for i in alphabet:
    deleteName = path+ "\\" + i+".txt"
    if(os.path.isfile(deleteName)):
        os.remove(deleteName)
