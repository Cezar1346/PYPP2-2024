import re

text = input()

new_text = re.sub(r"([A-Z])", lambda match: "_"+match.group(1).lower(), text)

print(new_text)