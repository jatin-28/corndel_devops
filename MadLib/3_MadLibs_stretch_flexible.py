import random
import re


def readPhraseFile(filename):
    f = open(filename)
    return f.read().splitlines()


tokenRegex = '%%(\\S+)%%'
token_marker = '__'
token = '%%' + token_marker + '%%'

# Choose a random phrase
phrases = readPhraseFile('phrases.txt')
random_phrase = random.choice(phrases)

# Ask for user input
tokenList = re.findall(tokenRegex, random_phrase)
tokenLookup = dict.fromkeys(tokenList)

for tokenType in tokenLookup:
    tokenLookup[tokenType] = input("Enter a {}: ".format(tokenType))

# Perform replacement
replacedPhrase = random_phrase

for tokenType in tokenLookup:
    token_replace = token.replace(token_marker, tokenType)
    replacedPhrase = replacedPhrase.replace(token_replace, tokenLookup[tokenType])

print(replacedPhrase)