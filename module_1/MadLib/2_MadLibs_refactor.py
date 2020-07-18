import random

token_marker = '__'
token = '%%' + token_marker + '%%'

# Read phrase file
filename = 'phrases.txt'
f = open(filename)
phrases = f.read().splitlines()

random_phrase = random.choice(phrases)

# Read user input
lookup = {"NOUN": input("Enter a noun: "),
          "VERB": input("Enter a verb: "),
          "ADJECTIVE": input("Enter a adjective: "),
          "ADVERB": input("Enter a adverb: ")
}

# Perform replacement
replacedPhrase = random_phrase

for tokenType in lookup:
    token_replace = token.replace(token_marker, tokenType)
    replacedPhrase = replacedPhrase.replace(token_replace, lookup[tokenType])

print(replacedPhrase)
