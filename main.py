import datetime
import os
import shutil


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.date.fromtimestamp(t)


path = input("Enter path: ")
if path == '':
    print("**** Insert a valid path to scan and reorganize. For example: C:/Users ****")
    exit(0)

files = os.listdir(path)

for file in files:
    # Se ho una directory non la processo
    if os.path.isdir(file):
        print(">>> Scarto seguente directory: " + str(file))
        continue
    filename, extension = os.path.splitext(file)
    print(">>> Processo il seguente file: " + filename)
    print("    >>> Data Creazione: " + str(modification_date(filename)))
    extension = extension[1:]

    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
