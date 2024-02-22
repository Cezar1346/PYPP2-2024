import re

text = input()

new_text = re.sub(r"_([a-z])", lambda match: match.group(1).upper(), text)

print(new_text)