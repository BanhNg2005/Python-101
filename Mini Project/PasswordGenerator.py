import secrets
import string

class Password:
    def __init__(self, length: int, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # Get characters from string module (the whole alphabet and all numbers from 0-9
        self.base_characters: str = string.ascii_lowercase + string.digits

        # If the user wants to use uppercase letters and symbols, add them to the base_characters string
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str: # returns the string a.k.a password
        password: list[str] = []

        # we have the length = 12, it is going to add 12 random characters to the password list
        for i in range(self.length):
            password.append(secrets.choice(self.base_characters)) # pick a random element from any iterable

        return ''.join(password) # convert the list into a string by return an empty string and join it all together

    def check_password(self):
        password = Password.generate(self)
    
        if len(password) < 16:
            return "password is too weak"
        
        if not any(char in string.ascii_uppercase for char in password):
            return "password is too weak"
        
        if not any(char in string.punctuation for char in password):
            return "password is too weak"
        
        return "password is strong"

def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=False)
    # or just simply do print(password.generate()) to print out the password

    for i in range(10):
        generated: str = password.generate()
        print(f'{generated} has {len(generated)} chars and {password.check_password()}' )

if __name__ == '__main__':
    main()

