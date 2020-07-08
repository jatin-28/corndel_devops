import random

token_marker = '__'
token = '%%' + token_marker + '%%'
filename = 'phrases.txt'
lookup = {}

f = open(filename)
phrases = f.read().splitlines()

random_phrase = random.choice(phrases)

lookup["NOUN"] = input("Enter a noun: ")
lookup["VERB"] = input("Enter a verb: ")
lookup["ADJECTIVE"] = input("Enter a adjective: ")
lookup["ADVERB"] = input("Enter a adverb: ")

replacedPhrase = random_phrase

for tokenType in lookup:
    token_replace = token.replace(token_marker, tokenType)
    replacedPhrase = replacedPhrase.replace(token_replace, lookup[tokenType])

print(replacedPhrase)
