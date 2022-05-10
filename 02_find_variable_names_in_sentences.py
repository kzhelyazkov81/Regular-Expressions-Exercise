import re

expression = r'\b_[A-Za-z0-9]+\b'
result = []
text = input()
names = re.findall(expression, text)

for name in names:
    result.append(name[1:])

print(','.join(result))
