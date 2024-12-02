import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def play_game():
    number_to_guess = random.randint(1, 100)
    print(number_to_guess)
    print('Guess a number between 1 and 100: ')
    difficulty = input("Choose difficulty, 'easy' or 'hard': ")

    if difficulty == 'easy':
        attemps = 10
    else:
        attemps = 5

    while attemps > 0:
        print(f'You have {attemps} remaining.')
        guess = int(input('Make a guess: '))
        if guess not in range(1,101):
            print('Only numbers between 1 and 100')
        elif guess > number_to_guess:
            print('Too high')
        elif guess < number_to_guess:
            print('Too low')
        elif guess == number_to_guess:
            print('You win!')
            attemps = 0
        attemps -= 1
        if attemps == 0:
            print(f'You lose, the number was {number_to_guess}')

while input('Want to guess number (y/n): ') == 'y':
    play_game()