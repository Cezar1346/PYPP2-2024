import re

string = input()

pattern = re.compile("[ .,]")

new_string = pattern.sub(":",  string)

print(new_string)


# pattern = re.compile(r"[Rr]egular")

# text_rows = pattern.sub("Irregular", text)

# print(text_rows)