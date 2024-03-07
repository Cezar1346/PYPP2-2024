import os

file = input().split()

with open(r"C:\\Users\\Cezar\\Desktop\\PY\\Lab6\\Dir-and-files\\1.text", "x") as f:
    f.write(" ".join(file))

os.remove(r"C:\\Users\\Cezar\\Desktop\\PY\\Lab6\\Dir-and-files\\1.text")
