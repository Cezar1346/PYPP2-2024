import os

path = "C:\\Users\\Cezar\\Desktop\\PY\\Lab6"

dir_list = os.listdir(path)

with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            print(entry.name)   
        else:
            print(entry.name)