import re

expression = r">>([A-Za-z]+)<<(\d+|\d+\.\d+)!(\d+)"
furnitures = []
total_cost = 0

while True:
    data = input()
    if data == 'Purchase':
        break
    result = re.match(expression, data)
    if result is not None:
        furniture = result[1]
        price = float(result[2])
        quantity = float(result[3])
        furnitures.append(furniture)
        total_cost += price * quantity

print('Bought furniture:')

if total_cost > 0:
    for name in furnitures:
        print(f'{name}')
print(f'Total money spend: {total_cost:.2f}')
