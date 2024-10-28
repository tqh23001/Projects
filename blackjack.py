import random

values = {'Ace': 1, 'Ace': 11, '2': 2,
          '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, '10': 10,
          'Kings': 10, 'Queens': 10, 'Jack': 10}

def random_card(): #Returns a random card
    return random.choice(list(values.keys()))

def game():
    end = False

    while not end:
        user_cards = [random_card(), random_card()] #Keeps track of player cards
        user_pts = values[user_cards[0]] + values[user_cards[1]] #Total player card value
        bot_cards = [random_card(), random_card()] #Keeps track of player cards
        bot_pts = values[bot_cards[0]] + values[bot_cards[1]] #Total bot card value
        print(f'The bot has {bot_cards[0]} and a mystery card')
        print(f'The bot has {values[bot_cards[0]]} points\n')
        print(f'You have {values[user_cards[0]]} and {values[user_cards[1]]}')
        print(f'You have {user_pts} points\n')
        choice = input('Would you like to hit or fold? (type hit or fold)')
        if choice.lower() == 'fold':
            user_diff = 21 - user_pts #Find the difference from 21
            bot_diff = 21 - bot_pts
            if bot_diff == user_diff:
                print(f'The bot has {bot_cards[0]} and {bot_cards[1]}')
                print(f'The bot has {bot_pts} points\n')
                print('You both tie!')
            elif bot_diff < user_diff:
                print(f'The bot has {bot_cards[0]} and {bot_cards[1]}')
                print(f'The bot has {bot_pts} points\n')
                print(f'The bot was closer to 21, you lose!')
            else:
                print(f'The bot has {bot_cards[0]} and {bot_cards[1]}')
                print(f'The bot has {bot_pts} points\n')
                print('You were closer to 21, you win!')



def main():
    print('Welcome to Black Jack!')
    game()
    print('purr')

if __name__ == '__main__':
    main()