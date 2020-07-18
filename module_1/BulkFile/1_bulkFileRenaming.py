import os
import sys
import shutil
import datetime

currentTime = datetime.datetime.now()
formattedDateTime = currentTime.strftime("%Y-%m-%dT%H%M%S")
print("Time to append: " + formattedDateTime)

path = 'temp'
if len(sys.argv) > 1:
    path = sys.argv[1]

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            filename = path + "/" + entry.name
            movedFile = shutil.move(filename, filename + "." + formattedDateTime)
            print("File: " + filename + " => " + movedFile)