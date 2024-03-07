import os

file = open(r"C:\\Users\\Cezar\\Desktop\\PY\\Lab6\\Builtin-functions\\1.py", "r")

with open(r"C:\\Users\\Cezar\\Desktop\\PY\\Lab6\\Dir-and-files\\1.text", "x") as new:
    for x in file:
        new.write(x)

os.remove(r"C:\\Users\\Cezar\\Desktop\\PY\\Lab6\\Dir-and-files\\1.text")