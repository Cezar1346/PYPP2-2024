import re

string = input()

print(re.findall("([a-z]+a[a-z]*b)", string))