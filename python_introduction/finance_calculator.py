# calculate user's monthly savings based on given income and expenses

income = int(input('Enter your monthly income: '))
expenses = int(input('Enter your total monthly expenses: '))

savings = income - expenses

projected_savings = int(savings * 12 + (savings * 0.05 * 12))  # assuming a 5% interest rate on savings

print('Your monthly savings are $', savings, '.', sep='')
print('Projected savings after one year, with interest, is: $', projected_savings, '.', sep='')