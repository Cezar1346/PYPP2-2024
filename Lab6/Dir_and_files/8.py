import os 

file = input()

if os.path.exists(file):
    os.remove(file)
    print("removed")
else:
    print("1488")