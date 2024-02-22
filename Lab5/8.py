import re

text = input()

new_text = re.findall(r"[A-Z][a-z]+", text)

print(new_text)