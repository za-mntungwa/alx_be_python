# calculate user's monthly savings based on given income and expenses

monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)  # assuming a 5% interest rate on savings

print('Your monthly savings are $', savings, '.', sep='')
print('Projected savings after one year, with interest, is: $', projected_savings, '.', sep='')
