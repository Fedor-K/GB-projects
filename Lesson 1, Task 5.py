income = int(input('Enter income'))
costs = int(input('Enter costs'))
profit = income - costs
if income > costs:
    print('Your company efficiency was', (((profit/income) / 1) * 100), '% this month')
else:
    print('Your company"s loss is', profit, '% this month')
FTE = int(input('Enter number of employees'))
FTE_profit = profit // FTE
print('Every employee efficiency was', FTE_profit, '% in average this month')
