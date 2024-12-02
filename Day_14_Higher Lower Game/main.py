import random
from game_data import data
import art

def get_random_famous():
    return data[random.randint(0,len(data)-1)]

def compare_followers(a, b):
    """
        return 0 if a > b, 1 if b > a, -1 equals
    """
    if a['follower_count'] > b['follower_count']:
        return 'A'
    elif a['follower_count'] < b['follower_count']:
        return 'B'
    else:
        return -1

game_over = False
points = 0
famous_a = get_random_famous()

while not game_over:
    print(art.logo)
    famous_b = get_random_famous()

    print(f'Compare A: {famous_a['name']}, a {famous_a['description']}, from {famous_a['country']} ' )
    print(art.vs)
    print(f'Against B: {famous_b['name']}, a {famous_b['description']}, from {famous_b['country']} ' )
    answer = input("Who has more followers? Type 'A' or 'B': " ).upper()
    most_followers = compare_followers(famous_a,famous_b)
    if answer == most_followers:
        points += 1
        print(f"You're right! Current score: {points}")
        if answer == 'B':
            famous_a = famous_b
    else:
        game_over = True
        print(f"You lose, total score: {points}")


