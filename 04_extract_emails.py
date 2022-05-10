import re

text = input()
expression = r'(^| )(?P<user>[a-zA-Z0-9]+((\.|,|_|\-)[a-zA-Z]+)*)@(?P<host>[A-Za-z]+(-[A-Za-z]+)*(\.[A-Za-z]+(-[A-Za-z]*)*)+)'
matches = re.finditer(expression, text)

for match in matches:
    user = match.group('user')
    host = match.group('host')
    print(f'{user}@{host}')

