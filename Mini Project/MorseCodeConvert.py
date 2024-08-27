morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', '?': '..--..', '"': '.-..-.', ',': '--..--', ':': '---...',
    '(': '-.--.', ')': '-.--.-', '%': '------..-.-----', '!': '-.-.--',
    '.': '.-.-.-', '-': '-....-', '=': '-...-', '/': '-..-.'
}
reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)
    # take one char at a time out of the text and inserting it into the get method
    # if it doesn't find that char, return an empty string

def convert_to_normal(morse: str) -> str:
    return ''.join(reverse_morse_code_dict.get(code, '') for code in morse.split(' '))
    # split the morse code into a list of codes, take one code at a time and insert it into the get method
    # if it doesn't find that code, return an empty string

def is_morse_code(input_text: str) -> bool:
    # check if the input contains only morse code characters
    return all(char in '.- /' for char in input_text) 

def main() -> None:
    user_input: str = input('Enter text: ')
    if is_morse_code(user_input):
        # if the input is Morse code, convert to normal text
        output: str = convert_to_normal(user_input)
        print(f"Morse to Text: {output}")
    else:
        # if the input is normal text, convert to morse code
        output: str = convert_to_morse(user_input)
        print(f"Text to Morse: {output}")

if __name__ == '__main__':
    main()