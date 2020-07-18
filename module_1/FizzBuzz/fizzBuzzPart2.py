def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

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

print ("============================")
print("FizzBuzz Part 2 - upto multiple 13")
for i in range(1, 200):
    toPrint = ""
    if i % 3 == 0: 
        toPrint = "Fizz"
    if i % 5 == 0: 
        toPrint = toPrint + "Buzz"
    if i % 7 == 0:
        toPrint = toPrint + "Bang"
    if i % 11 == 0:
        toPrint = "Bong"
    if i % 13 == 0:
        try:
            index = toPrint.index("B")
            toPrint = insert(toPrint, "Fezz", index)
        except:
            toPrint = toPrint + "Fezz"

    if len(toPrint) > 0:
        print(toPrint)
    else:
        print (i)


print ("============================")
print("FizzBuzz Part 2 with multiple 17 using lists")
numbers = int(input("Enter maximum number: "))
for i in range(1, numbers + 1):
    toPrint = []
    if i % 3 == 0: 
        toPrint.append("Fizz")
    if i % 5 == 0: 
        toPrint.append("Buzz")
    if i % 7 == 0:
        toPrint.append("Bang")
    if i % 11 == 0:
        toPrint = ["Bong"]
    if i % 13 == 0:
        toPrint = searchAndInsertAtPos(toPrint, "B", "Fezz")
    if i % 17 == 0:
        toPrint.reverse()

    if toPrint:
        print( "".join(toPrint))
    else:
        print (i)