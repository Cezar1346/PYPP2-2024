import re

word = input()

print(re.findall("abbb?", word))