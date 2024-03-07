string = input()

def cntr(string):
    str_is_upper = 0
    str_is_lower = 0
    for x in string:
        if x.isupper():
            str_is_upper += 1
    for x in string:
        if x.islower():
            str_is_lower += 1
    print(str_is_upper)
    print(str_is_lower)

cntr(string)