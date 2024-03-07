import os

path = "C:\\Users\\Cezar\\Desktop\\PY"

if os.access(path, os.F_OK):
    if os.access(path, os.R_OK):
        if os.access(path, os.W_OK):
            if os.access(path, os.X_OK):
                print("file exist, readable, writable and executable")
else:
    print(os.listdir(path))

print(os.listdir(path))