import json

# load the rates from a json file
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)

# rates uses dict data type which is from the json file
def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base: str = base.lower()
    to: str = to.lower()

    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    try:
        if base == 'eur':
            return amount * to_rates['rate']
        elif base == "eur":
            return amount * to_rates['rate'] / from_rates['rate']
        elif to == "eur":
            return amount / from_rates['rate']
        else:
            return amount / from_rates['rate'] * to_rates['rate']
    except TypeError:
        print('Please enter a valid currency!')
        print(f'Existed currency: {list(rates.keys())} ')


def main() -> None:
    rates: dict[str, dict] = load_rates('rates.json')
    result: float = convert(amount=10, base='cad', to='eur', rates=rates)
    print(result)

if __name__ == '__main__':
    main()