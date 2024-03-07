word1 = input()
word2 = ''.join(reversed(word1))

def checker(word1, word2):
    return word1 == word2

if checker(word1, word2):
    print("Yes!")
else:
    print("No!")