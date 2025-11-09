# Personal Finance Calculator

# Collects user info
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

# Calculates monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projects annual savings
annual_interest_rate = 0.05
projected_savings = ((monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate))

# Prints monthly savings and projected annual savings
print('Your monthly savings are {}'.format(monthly_savings))
print('Projected savings after one year, with interest, is: {:.0f}.'.format(projected_savings))
