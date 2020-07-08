import random
import re

tokenRegex = '%%(\\S+)%%'
token_marker = '__'
token = '%%' + token_marker + '%%'
filename = 'phrases.txt'

f = open(filename)
phrases = f.read().splitlines()

random_phrase = random.choice(phrases)

tokenList = re.findall(tokenRegex, random_phrase)
tokenLookup = dict.fromkeys(tokenList)

for tokenType in tokenLookup:
    tokenLookup[tokenType] = input("Enter a {}: ".format(tokenType))

replacedPhrase = random_phrase

for tokenType in tokenLookup:
    token_replace = token.replace(token_marker, tokenType)
    replacedPhrase = replacedPhrase.replace(token_replace, tokenLookup[tokenType])

print(replacedPhrase)
