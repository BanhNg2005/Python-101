import requests

oxford_app_id = "df191c49"
oxford_app_key = "a2b9e13a85dfad3dcac371a4a5e99611"

# Get the random word with the specified length
def get_wordlength(length):
    url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-gb"
    headers = {
        "app_id": oxford_app_id,
        "app_key": oxford_app_key
    }
    params = {
        "word_length": length
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        words_data = response.json()
        print("API Response:", words_data)  # Debugging line to inspect the response
        # Assuming the API returns a list of words, you might need to adjust based on actual response structure
        words = words_data.get("results", [])
        if words:
            # Select a random word from the list if multiple words are returned
            return words[0].get("word")  # Adjust based on the actual key for the word in the response
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response content:", response.content)  # Debugging line to inspect the error response
    return None

# Get a random word with exactly 5 letters
random_word = get_wordlength(5)
print("Random Word:", random_word)  # Debugging line to check the fetched word

def main():
    print("Welcome to wordle clone :)")
    print("You have 6 attempts to guess the word.")
    attempts = 6
    while attempts > 0:
        guess = input("Enter your guess: ")
        if len(guess) != 5:
            print(f"Please enter a word with exactly 5 letters. You still have {attempts} attempts.")
            continue
        attempts -= 1  # Decrement attempts only if the guess is valid
        if guess == random_word:
            print(f"Congratulations! You have guessed the word {random_word} in {6 - attempts} attempts.")
            break
        elif guess != random_word:
            print(f"Sorry! Your guess is incorrect. You have {attempts} attempts")
    else: # This block will run if the while loop completes without breaking
        print(f"Sorry! You have run out of attempts. The word was {random_word}")

if __name__ == "__main__":
    main()