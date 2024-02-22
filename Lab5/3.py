import re

word = input()

print(re.findall("[a-z_]", word))