from difflib import SequenceMatcher
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

def configure() -> None:
    load_dotenv()

configure()

api_key = os.getenv("API_KEY1")
api_url = 'https://api.openweathermap.org/data/2.5/weather?'

def load_weather(city: str) -> dict:
    url = f'{api_url}appid={api_key}&q={city}&units=metric'
    r = requests.get(url)
    return r.json()

class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity: float = 0.0
        best_match: str = 'Sorry, I didn\'t understand that'

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match: str = self.responses[response]

        return best_match, highest_similarity

    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you today?')

        while True:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)
            if similarity < 0.5:
                print('I don\'t understand! Could you please rephrase it or you can ask me another question :)')
            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'
            elif response == 'weather':
                city = input('Enter the city name (e.g., London,uk): ')
                weather_data = load_weather(city)
                if weather_data.get('cod') == 200:
                    temp = weather_data['main']['temp']
                    description = weather_data['weather'][0]['description']
                    response = f"The weather in {city.title()} is {description} with a temperature of {temp}°C."
                else:
                    response = f"Sorry, I couldn't retrieve the weather for {city.title()}."

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')

            if 'bye' in user_input.lower() or 'see you' in user_input.lower():
                break

def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'What time is it': 'GET_TIME',
        'weather': 'weather',
        'bye': 'Goodbye! Have a great day',
        'see you again': 'See you next time :D',
        'can you tell me a joke': 'Sure, here is one that I have! Why was 10 scared? He was in the middle of 9-11',
        'who are you?': 'My name is Lmao, and I am your assistant. Feel free to ask me if you have any question!',
        'in what language do you assist?': 'I am able to assist you in English, French, and Vietnamese',
        'French': 'Ça roule? Comment puis-je vous aider aujourd\'hui',
        'Vietnamese': 'Chào bạn, bạn có khỏe không? Tôi có thể giúp gì cho bạn nhỉ.'
    }

    chatbot: ChatBot = ChatBot(name='Lmao', responses=responses)
    chatbot.run()

if __name__ == '__main__':
    main()