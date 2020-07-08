import random

filename = 'phrases.txt'

f = open(filename)
phrases = f.read().splitlines()

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter a adjective: ")
adverb = input("Enter a adverb: ")

random_phrase = random.choice(phrases)

replacedPhrase = random_phrase.replace("%%NOUN%%", noun).replace("%%ADJECTIVE%%", adjective).replace("%%VERB%%", verb).replace("%%ADVERB%%", adverb)

print (replacedPhrase)