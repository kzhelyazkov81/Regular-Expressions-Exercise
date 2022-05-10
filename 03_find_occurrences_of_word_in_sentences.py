import re

text = input()
word = input()

expression = rf'\b{word}\b'

result = re.findall(expression, text, re.I)

print(len(result))

