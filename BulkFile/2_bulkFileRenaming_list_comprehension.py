import os
import sys
import shutil
import datetime


def movefile(datetimestr, x, path):
    filename = path + "/" + x.name
    return shutil.move(filename, filename + "." + datetimestr)


currentTime = datetime.datetime.now()
formattedDateTime = currentTime.strftime("%Y-%m-%dT%H%M%S")

path = 'temp'
if len(sys.argv) > 1:
    path = sys.argv[1]

output = [movefile(formattedDateTime, x, path) for x in os.scandir(path) if x.is_file()]

print("Time to append: " + formattedDateTime)
print("Files moved: ")

[print(x) for x in output]

