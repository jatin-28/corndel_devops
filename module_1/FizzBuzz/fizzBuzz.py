print("First way:")
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz") 
    elif i % 3 == 0: 
        print ("Fizz")
    elif i % 5 == 0: 
        print ("Buzz")
    else:
        print (i)

print("\n\n=======================")
print("Second way:")
for i in range(1, 100):
    toPrint = ""
    if i % 3 == 0: 
        toPrint = "Fizz"
    if i % 5 == 0: 
        toPrint = toPrint + "Buzz"
    if len(toPrint) > 0:
        print(toPrint)
    else:
        print (i)

