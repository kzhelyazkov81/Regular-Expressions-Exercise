import re

while True:
    text = input()
    if not text:
        break
    numbers = re.findall(r'\d+', text)
    if len(numbers) > 0:
        print(' '.join(numbers), end=' ')

