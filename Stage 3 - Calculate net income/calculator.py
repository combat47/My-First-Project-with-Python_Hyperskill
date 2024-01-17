# This is Amirhossein Jahazi ;)

products = {'Bubblegum': 202,
            'Toffee': 118,
            'Ice cream': 2250,
            'Milk chocolate': 1680,
            'Doughnut': 1075,
            'Pancake': 80}

total_income = sum(products.values())
print('Earned amount:')
for key, value in products.items():
    print(f'{key}: ${value}')
print()
print(f'Income: ${total_income}')

staff_expenses = int(input("Staff expenses: \n"))
other_expenses = int(input("Other expenses: \n"))
total_income -= staff_expenses + other_expenses
print("Net income: $", total_income, sep='')
