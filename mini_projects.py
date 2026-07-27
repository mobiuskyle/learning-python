## mini project one - personal finance snapshot
monthly_income=int(input('Enter your monthly income : '))
monthly_expense = int(input('Enter your total monthly expenses : '))
savings = monthly_income-monthly_expense
percentage_saved = (savings/monthly_income)*100
print('Monthly Income : ',monthly_income)
print('Monthly Expenses : ',monthly_expense)
print('Savings : ',savings)
if percentage_saved>20:
    print(f"Great Job.You're saving {percentage_saved}% of your Income ")
elif percentage_saved>=0 and percentage_saved <=20:
    print(f"You have saved {percentage_saved}% of your Income but Consider cutting some expenses")
elif percentage_saved < 0 :
    print("WARNING!WARNING!YOU ARE SPENDING MORE THAN YOU EARN !")