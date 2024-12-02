import random
import art








def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))



    print(f'Yuor cards: {user_cards}, current score: {calculate_score(user_cards)}')
    print(f'Computer first card: {computer_cards[0]}')

    next_card = input('Want another card? (y/n): ')

    while next_card == 'y':
        user_cards.append(random.choice(cards))
        print(f'Yuor cards: {user_cards}, current score: {calculate_score(user_cards)}')
        if calculate_score(user_cards) > 21:
            # print('You lose')
            next_card = 'n'
        else:
            print(f'Computer first card: {computer_cards[0]}')
            next_card = input('Want another card? (y/n): ')

    while calculate_score(computer_cards) !=0 and calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    
    # print(f'Yuor cards: {user_cards}, current score: {calculate_score(user_cards)}')
    print(f'Computer cards: {computer_cards}, current score: {calculate_score(computer_cards)}')
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))

while input('Start the game? (y/n): ') == 'y':
    play_game()