import random

choices = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}


def game():
    player_points = 0
    computer_points = 0
    print("Welcome! Let's play")
    player_name = input("But first, tell me your name:  ")
    print(f"And now {player_name}, choose your weapon!")
    while True:
        player_choice = input('[r]ock, [p]aper, [s]cissors: ')
        computer_choice = random.choice(list(choices.keys()))
        print(computer_choice)
        if player_choice == computer_choice:
            print("It's a draw! No points")
        elif player_choice == 'r':
            if computer_choice == 'p':
                print("Sorry but this time I won")
                computer_points += 1
            else:
                print("Point for you")
                player_points += 1
        elif player_choice == 'p':
            if computer_choice == 's':
                print("Sorry but this time I won")
                computer_points += 1
            else:
                print("Point for you")
                player_points += 1
        elif player_choice == 's':
            if computer_choice == 'r':
                print("Sorry but this time I won")
                computer_points += 1
            else:
                print("Point for you")
                player_points += 1
        if player_points == 3 or computer_points == 3:
            print(f'{player_points}, {computer_points}')
            play_again = input("Do you wanna play again? [y]/[n]: ")
            if play_again.lower() == 'y':
                player_points = 0
                computer_points = 0
                continue
            else:
                break


game()
