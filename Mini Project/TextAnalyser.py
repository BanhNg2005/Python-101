from collections import Counter

def open_file(path: str) -> str: # return the contents of the note (or text)
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyse(text: str) -> dict[str, int]:
    print(f'"{text}"')
    print('-------------')
    words = text.lower().split()
    word_counts = Counter(words) # Count the occurrences of each word in the text
    top_5_common_words = word_counts.most_common(5)

    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')), # replace every space with an empty space
        'total_spaces': text.count(' '),
        'total_words': len(words),
        'top_5_common_words': top_5_common_words
    }

    return result

def main() -> None:
    text: str = open_file('note.txt')
    analysis: dict[str, int] = analyse(text)

    for key, value in analysis.items():
        if key == 'total_chars_incl_spaces':
            print(f'This text file contains {value} total characters (including spaces).')
        elif key == 'total_chars_excl_spaces':
            print(f'This text file contains {value} total characters (excluding spaces).')
        elif key == 'total_spaces':
            print(f'This text file contains {value} spaces.')
        elif key == 'total_words':
            print(f'This text file contains {value} words.')
        else:
            print(f'The top 5 most common words are: {value}')

if __name__ == '__main__':
    main()