import re

def splitUpperCase(string):
    for i in string:
        x = re.sub(r'([a-z])([A-Z])', r'\1 \2', i)
        print(x)

testString = ["asdAsdaAd", "adwAdwaddVadsAWfa"]

splitUpperCase(testString)
