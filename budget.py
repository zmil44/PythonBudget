def main():
    budget=int(input('Enter your budget: '))
    months=int(input('enter amount of months: '))
    expenses=0
    count=1
    while(count<=months):
        monthExpenses=int(input('enter your expenses for the month: $'))
        expenses=expenses+monthExpenses
        count=count+1
    display(budget,expenses)

def display(budget, expenses):
    over_under=budget-expenses
    if (budget<expenses):
        print('You are over budget $',over_under)
    elif (budget>= expenses):
        print('You under budget by $',over_under)
main()
