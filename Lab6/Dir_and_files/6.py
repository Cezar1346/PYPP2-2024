import os

path_to_folder = r"C:\\Users\\Cezar\\Desktop\\PY\\Lab6\\builtin-functions"

for i in range(65, 91):
    open(f"{chr(i)}.txt", "x")
