import requests
from dotenv import load_dotenv
import os


# Load environment variables from .env file
def configure() -> None:
    load_dotenv()


# Call the configure function to load the environment variables
configure()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Construct the API URL with the API key
api_url = f'https://api.exchangeratesapi.io/v1/latest?access_key={api_key}&format=1'

response = requests.get(api_url)

print('Welcome to the ExchangeRate')


# Load rates from the API
def load_rates() -> dict:
    return response.json()


# This function will convert the amount from one currency to another
def convert(amount: float, base: str, to: str, rates: dict) -> float:
    base = base.upper()
    to = to.upper()

    from_rate = rates.get('rates').get(base)
    to_rate = rates.get('rates').get(to)

    if base == 'EUR':
        return amount * to_rate
    elif to == 'EUR':
        return amount / from_rate
    else:
        return amount / from_rate * to_rate


def main() -> None:
    rates = load_rates()
    if rates is None:
        print("Failed to load exchange rates. Exiting.")
        return

    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount > 0:
                break
            else:
                print('Invalid input. Please enter a positive number.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    while True:
        base = input('Enter the base currency: ').upper().strip()
        if base in rates.get('rates'):
            break
        else:
            print('Invalid input. Please enter a valid currency.')
            print(f'Existed currency: {list(rates.get("rates").keys())} ')

    while True:
        to = input('Enter the currency to convert to: ').upper().strip()
        if to in rates.get('rates'):
            break
        else:
            print('Invalid input. Please enter a valid currency.')
            print(f'Existed currency: {list(rates.get("rates").keys())} ')

    result = convert(amount=amount, base=base, to=to, rates=rates)
    print(f'{amount:.2f} {base} is equal to {result:.2f} {to} on the exchange rate of {rates.get("date")}.')


if __name__ == '__main__':
    main()