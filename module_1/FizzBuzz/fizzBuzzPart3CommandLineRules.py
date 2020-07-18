import sys

def appendToList(x, stringToAppend):
    x.append(stringToAppend)
    return x

def reverseList(x):
    x.reverse
    return x

# insert stringToInsert at the position found by stringToFind
# otherwise if not found append
def searchAndInsertAtPos(x, stringToFind, stringToInsert):
    hasSet = False
    for element in x:
        index = element.find(stringToFind)
        if index > -1:
            hasSet = True
            toPrint.insert(index + 1, stringToInsert)
            break
    if not hasSet:
        x.append(stringToInsert)
    return x

rules = {
    '3' : (lambda x : appendToList(x,"Fizz")),
    '5' : (lambda x : appendToList(x,"Buzz")),
    '7' : (lambda x : appendToList(x,"Bang")),
    '11': (lambda x : ["Bong"]),
    '13': (lambda x : searchAndInsertAtPos(x, "B", "Fezz")),
    '17': (lambda x: reverseList(x))
}

print("FizzBuzz - Using rules")
print("Command line rule arguments (e.g. 3 5) or empty for all: ", rules.keys())
if len(sys.argv) < 2:
    args = rules.keys()
else:
    args = sys.argv[1:]

print('Running rules:', args)

numbers = int(input("Enter maximum number: "))
for i in range(1, numbers + 1):
    toPrint = []
    
    for key in args:
        try:
            if i % int(key) == 0:
                toPrint = rules[key](toPrint)
        except:
            print("Invalid rule: ", key)

    if toPrint:
        print( "".join(toPrint))
    else:
        print (i)