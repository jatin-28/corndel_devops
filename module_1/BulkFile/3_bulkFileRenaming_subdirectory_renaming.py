import os
import sys
import shutil
import datetime


def movefile(datetimestr, xFile, path):
    filename = os.path.join(path, xFile)
    return shutil.move(filename, filename + "." + datetimestr)


currentTime = datetime.datetime.now()
formattedDateTime = currentTime.strftime("%Y-%m-%dT%H%M%S")

path = 'temp3'
if len(sys.argv) > 1:
    path = sys.argv[1]

output = [movefile(formattedDateTime, f, root) for root, _, files in os.walk(path, topdown=False) for f in files]
outputDirs = [movefile(formattedDateTime, d, root) for root, dirs, _ in os.walk(path, topdown=False) for d in dirs]

print("Time to append: " + formattedDateTime)
print("Files moved: ")
[print(x) for x in output]

print("Dirs moved: ")
[print(x) for x in output]
