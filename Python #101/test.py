
def locate_cards(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Time complexity: O(n) because the while loop runs n times where n is the length of the cards list
