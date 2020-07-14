import os
import sys
import shutil
import datetime


def movefile(datetimestr, xFile, path):
    filename = os.path.join(path, xFile)
    return shutil.move(filename, filename + "." + datetimestr)


currentTime = datetime.datetime.now()
formattedDateTime = currentTime.strftime("%Y-%m-%dT%H%M%S")

path = 'temp10'
if len(sys.argv) > 1:
    path = sys.argv[1]

output = [movefile(formattedDateTime, f, root) for root,dirs,files in os.walk(path, topdown=False) for f in files]

print("Time to append: " + formattedDateTime)
print("Files moved: ")

[print(x) for x in output]

