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

def convertToGramms(gramms):
    x = gramms * 28.3495231
    return x

ouncies = float(input("Enter ouncies to convert: "))
print(ouncies, " ouncies in gramms is: ", convertToGramms(ouncies), " gramms.")


'''
*
*
*
Ex 2
*
*
*
'''
def convertToCelsium(F):
    C = (5 / 9) * (F - 32)
    return C


F = float(input("Enter F to convert: "))
print(F, " farenheit in celsium is: ", convertToCelsium(F), " celsium.")


'''
*
*
*
Ex 3
*
*
*
'''

def solve(heads, legs):
    for x in range(heads + 1):
        y = heads - x
        totalLegs = 2 * x + 4*y
        if totalLegs == legs:
            return x, y
    return "No solution"

heads = 36
legs = 98
result = solve(heads, legs)
print("chickens: ",result[0])
print("rabbits: ", result[1])

'''
*
*
*
Ex 4
*
*
*
'''


def is_prime(num):
    for a in range(1, int(math.sqrt(num)) + 1):
        if num % a == 0:
            return False
        else:
            return True

numList = [1,2]
x = int(input())
for a in range(x):
    a = 2
    numList.append(a+1)
primeList = list(filter(lambda num: is_prime(num), numList))

print(primeList)


'''
*
*
*
Ex 5
*
*
*
'''
def permutations(string):
    # Base case: if the string has only one character, return it as a single-item list
    if len(string) == 1:
        return [string]
    
    # List to store permutations
    perms = []
    
    # Iterate through each character in the string
    for i in range(len(string)):
        # Fix the current character and recursively generate permutations for the remaining characters
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in permutations(remaining_chars):
            perms.append(fixed_char + perm)
    
    return perms

# Test the function
user_input = input("Enter a string: ")
perms = permutations(user_input)
print("Permutations of the string:")
for perm in perms:
    print(perm)
'''
*
*
*
Ex 6
*
*
*
'''
def reversed_words(sentence):
    sentence += " "
    words_in_sentence = []
    word = ""
    for letter in range(len(sentence)):
        if(sentence[letter]== " "):
            words_in_sentence.append(word)
            word = ""
        else:
            word += sentence[letter]
    for words in reversed(words_in_sentence):
        print(words)

user_input = input("Write your sentence: ")
print("reversed sentence of yours: ")
reversed_words(user_input)


'''
*
*
*
Ex 7
*
*
*
'''
def has_33(nums):
    b = False
    for i in range(len(nums)-1):
        if(nums[i] == 3 and nums[i + 1] == 3):
            b = True
        else:
           continue
    print(b)

has_33([1, 3, 3])
has_33([1,3,2,4,3,3,2,1])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 
'''
*
*
*
Ex 8
*
*
*
'''
def spy_game(nums):
    b = False
    zero_cnt = 0
    for i in nums:
        if(i == 0):
            zero_cnt += 1
        elif(i == 7 and zero_cnt >= 2):
            b = True
    print(b)

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

'''
*
*
*
Ex 9
*
*
*
'''
def volume(radius):
    return 4/3 * math.pi * radius**3

print(volume(3))

'''
*
*
*
Ex 10
*
*
*
'''

def unique_list(f_list):
    s_list = []
    for i in f_list:
        
        if(i not in s_list):
                s_list.append(i)
    return s_list
print(unique_list([1,2,1,3,49,2,4,19,14]))

'''
*
*
*
Ex 11
*
*
*
'''
def check_palindrome(string):
    
    if(string == string[::-1]):
        return True
    else: 
        return False
    

print(check_palindrome("madam"))

'''
*
*
*
Ex 12
*
*
*
'''
def histogram(nums):
    for i in nums:
        print("*"*i)
    return

histogram([4, 9, 7])

'''
*
*
*
Ex 13
*
*
*
'''
import random 
def guess_num():
    guessed_num = random.randint(1,20)
    guesses = 0
    
    print("Hello! What is your name?")
    name = input()
    print('''Well,''',name,''', I am thinking of a number between 1 and 20.''')
    print("Take a guess")
    while True:
        num = int(input())
        if(num == guessed_num):
            print("Good job,", name, "! You guessed my number in ", guesses," guesses!")
            break
        else:
            if(num < guessed_num):
                print("Your guess is too low.")
                print("Take a guess")
                guesses +=1
            elif(num > guessed_num):
                print("Your guess is too high.")
                print("Take a guess")
                guesses +=1


guess_num()

'''
*
*
*
Ex 14
*
*
*
'''