import re

expression = r'(?P<sub_domain>[w]{3})\.(?P<domain>[A-Za-z0-9-]+)(?P<domain_extension>(\.[a-z]+)+)'

while True:
    text = input()
    if not text:
        break
    matches = re.finditer(expression, text)
    for match in matches:
        sub_domain = match.group('sub_domain')
        domain = match.group('domain')
        domain_extension = match.group('domain_extension')
        print(f'{sub_domain}.{domain}{domain_extension}')
