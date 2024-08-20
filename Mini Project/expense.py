from typing import List

def calculate_split(total_amount: float, splits: List[int], currency: str) -> None:
    if len(splits) < 1:
        raise ValueError('At least one split percentage must be provided.')

    total_split_amount = sum(splits)
    if total_split_amount != 100:
        raise ValueError('The sum of all split percentages must equal 100%.')

    print(f'Total expense: {currency}{total_amount:,.2f}')
    for i, split_amount in enumerate(splits):
        share_per_person = total_amount * split_amount / 100
        print(f'Person {i + 1} ({split_amount}%): {currency}{share_per_person:,.2f}')


def main() -> None:
    while True:
        try:
            total_amount: float = float(input('Enter the total amount of the expense: '))
            if total_amount > 0:
                break
            else:
                print('Invalid input. Please enter a positive number.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    while True:
        splits_input: str = input('Enter the split amounts (e.g., 20, 40, 40): ')
        try:
            splits: List[int] = [int(x.strip()) for x in splits_input.split(',')]
            if sum(splits) == 100:
                break
            else:
                print('The sum of all split percentages must equal 100%.')
        except ValueError:
            print('Invalid input. Please enter a comma-separated list of integers.')

    calculate_split(total_amount, splits, currency='USD')


if __name__ == '__main__':
    main()