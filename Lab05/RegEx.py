'''
Ex 1
'''
import re

def match_string(test_string):
    txt = test_string
    for i in txt:
        x = re.search("ab", i)
        if x:
            print(f'This text has the pattern: ', i)
        else:
            print(f'This text has not the pattern: ', i)

# Test cases
test_strings = ["ab", "abb", "a", "abbbb", "b", "ba", "acb"]
match_string(test_strings)


'''
Ex 2
'''
def match_2_or_3_b(test_string):
    txt = test_string
    for i in txt:
        x = re.findall(r"\ba + _{2,3}b\b")
        if x:
            print(f'This text has the pattern: ', i)
        else:
            print(f'This text has not the pattern: ', i)


# Test cases
test_strings = ["ab", "abb", "a", "abbb", "b", "ba", "acb"]
match_2_or_3_b(test_strings)

'''
Ex 3
'''

def match_2_or_3_b(test_string):
    txt = test_string
    for i in txt:
        x = re.findall(r'\b[a-z]+_[a-z]+\b', i)
        if x:
            print(f'This text has the pattern: ', i)
        else:
            print(f'This text has not the pattern: ', i)


# Test cases
test_strings = ["ab", "a_bb", "a_", "ab_bb", "_b", "b_a", "acb"]
match_2_or_3_b(test_strings)


'''
Ex 4
'''

import re

def match_upper_lower(test_strings):
    for test_string in test_strings:
        x = re.findall(r'\b[A-Z][a-z]+\b', test_string)
        if x:
            print(f'This text has the pattern: {test_string}')
        else:
            print(f'This text does not have the pattern: {test_string}')


# Test cases
test_strings = ["Ab", "A_bb", "AAbb", "aAbbb", "B", "ba", "Acb"]
match_upper_lower(test_strings)

'''
Ex 5
'''
def match_2_or_3_b(test_string):
    txt = test_string
    for i in txt:
        x = re.findall(r'\bab\b', i)
        if x:
            print(f'This text has the pattern: ', i)
        else:
            print(f'This text has not the pattern: ', i)


# Test cases
test_strings = ["ab", "a_bb", "a_", "ab_bb", "_b", "b_a", "acb"]
match_2_or_3_b(test_strings)

'''
Ex 6
'''

def match_2_or_3_b(test_string):
    txt = test_string
    for i in txt:
        x = re.sub("\W", ":", i)
        print(x)


# Test cases
test_strings = ["a b", "a,bb", "a.", "ab.bb", ".b", "b a", "a c b"]
match_2_or_3_b(test_strings)


'''
Ex 7
'''
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0]
    for word in words[1:]:
        camel_case += word.capitalize()
    return camel_case
snake_string = "this_is_snake_case_example"
camel_string = snake_to_camel(snake_string)
print(camel_string)

'''
Ex 8
'''

def splitUpperCase(string):
    for i in string:
        x = re.sub(r'([a-z])([A-Z])', r'\1 \2', i)
        print(x)

testString = ["asdAsdaAd", "adwAdwaddVadsAWfa"]

splitUpperCase(testString)

'''
Ex 9
'''
def splitUpperCase(string):
    for i in string:
        x = re.sub(r'([a-z])([A-Z])', r'\1 \2', i)
        print(x)

testString = ["asdAsdaAd", "adwAdwaddVadsAWfa"]

splitUpperCase(testString)

'''
Ex 10
'''
a = "ThisIsCamelCaseExample"
res = '_'.join(re.findall('[a-z]+|[A-Z][a-z]*', a)).lower()
print(res)