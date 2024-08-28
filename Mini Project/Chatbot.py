from difflib import SequenceMatcher
from datetime import datetime

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
            if similarity > highest_similarity: # if the similarity is higher than the previous highest similarity
                highest_similarity = similarity # set the highest similarity to the current similarity
                best_match: str = self.responses[response] # set the best match to the response

        return best_match, highest_similarity

    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you today?')

        while True:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H%M}'

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')

            if 'bye' in user_input.lower() or 'see you' in user_input.lower():
                break

def main() -> None:
        responses: dict[str, str] = {
            'hello': 'Hello! How are you today?',
            'how are you': 'Great, thanks! What about you?',
            'What time is it': 'GET_TIME',
            'bye': 'Goodbye! Have a great day',
            'see you again': 'See you next time :D',
            'can you tell me a joke': 'Sure, here is one that I have! Why was 10 scared? He was in the middle of 9-11',
            'who are you?': 'My name is Lmao, and I am your assistant. Feel free to ask me if you have any question!',
            'in what language do you assist?': 'I am able to assist you in English, French, and Spanish'

        }

        chatbot: ChatBot = ChatBot(name='Lmao', responses=responses)
        chatbot.run()  

if __name__ == '__main__':
    main()