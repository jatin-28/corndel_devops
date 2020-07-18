import random

# Read phrase file
filename = 'phrases.txt'

f = open(filename)
phrases = f.read().splitlines()

# Get user input
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter a adjective: ")
adverb = input("Enter a adverb: ")

# Perform replacement
random_phrase = random.choice(phrases)
replacedPhrase = random_phrase.replace("%%NOUN%%", noun).replace("%%ADJECTIVE%%", adjective).replace("%%VERB%%", verb).replace("%%ADVERB%%", adverb)

print (replacedPhrase)