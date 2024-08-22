from collections import Counter
import re

# -> means this will return from the function
# tuple is going to hold the word and the amount of occurrences
def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common(n=10)  # n=10 means only showcase the top 10 common words

def read_txt_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file: # using with statement to open the file
        return file.read() # read the file and return the content

def main() -> None:
    choice = input('Do you want to enter text manually or read from a file? (enter/file): ').strip().lower()
    if choice == 'file':
        file_path = input('Enter the file path: ').strip()
        try:
            text = read_txt_file(file_path)
        except Exception as e:
            print(f'Error reading file: {e}')
            return
    else:
        text = input('Enter your text: ').strip()

    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies:
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()