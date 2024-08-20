# everything in the parenthesis is called type notation and the None just means to execute
# the function and do not return anything
def calculate_finances(monthly_income: float, tax_rate: float, currency: str, monthly_expenses: float) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    monthly_savings: float = monthly_net_income - monthly_expenses
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_savings: float = monthly_savings * 12

    print('-----------------------')
    print(f"Monthly income: {currency}{monthly_income:,.2f}")
    print(f"Tax rate: {tax_rate:,.0f}%")
    print(f"Monthly tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly net income: {currency}{monthly_net_income:,.2f}")
    print(f"Monthly savings: {currency}{monthly_savings:,.2f}")
    print(f"Yearly salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly tax paid: {currency}{yearly_tax:,.2f}")
    print(f"Yearly net income: {currency}{yearly_net_income:,.2f}")
    print(f"Yearly savings: {currency}{yearly_savings:,.2f}")

# no longer pollute the global scope when putting code in the function
def main() -> None:
    while True:
        try:
            monthly_income: float = float(input('Enter your monthly salary: '))
            break
        except (ValueError, TypeError):
            print('Invalid input. Please enter a valid number for monthly salary.')

    while True:
        try:
            tax_rate: float = float(input('Enter your tax rate (%): '))
            break
        except (ValueError, TypeError):
            print('Invalid input. Please enter a valid number for tax rate.')
    while True:
        try:
            monthly_expenses: float = float(input('Enter your monthly expenses: '))
            break
        except (ValueError, TypeError):
            print('Invalid input. Please enter a valid number for monthly expenses.')

    while True:
        currency: str = input('Enter your currency: ')
        if currency.isalpha():
            break
        else:
            print('Invalid input. Please enter a valid currency using alphabetic characters only.')

    calculate_finances(monthly_income, tax_rate, currency, monthly_expenses)

# this check will make sure this code will only run
# if we run this code directly
if __name__ == '__main__':
    main()