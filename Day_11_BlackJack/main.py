import random
# import arty


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []



start = input('Start the game? (y/n): ')

# while start == 'y':
for _ in range(2):
    user_cards.append(random.choice(cards))

computer_cards.append(random.choice(cards))

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

print(f'Yuor cards: {user_cards}, current score: {calculate_score(user_cards)}')
print(f'Computer first card: {computer_cards[0]}')

next_card = input('Want another card? (y/n): ')

while next_card == 'y':
    user_cards.append(random.choice(cards))
    print(f'Yuor cards: {user_cards}, current score: {calculate_score(user_cards)}')
    if calculate_score(user_cards) > 21:
        print('You lose')
        next_card = 'n'
    elif calculate_score(user_cards) == 21:
        print('You Win!')
        next_card = 'n'
    else:
        print(f'Computer first card: {computer_cards[0]}')
        next_card = input('Want another card? (y/n): ')




