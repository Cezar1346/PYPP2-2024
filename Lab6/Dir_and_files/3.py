import os 

something = input()

if os.path.exists(something):
    print(os.path.basename(something))
    print(os.path.dirname(something))
else:
    print("nothing")