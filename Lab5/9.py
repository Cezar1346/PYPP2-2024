import re

text = input()

new_text = re.sub(r"([A-Z])", lambda match: " "+match.group(1), text)

print(new_text)