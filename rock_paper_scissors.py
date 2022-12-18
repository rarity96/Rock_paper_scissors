import random

def get_player_move():
    while True:
        player_move = input("Choose your weapon, rock, paper, scissors: ")
        if player_move in ['paper', 'rock', 'scissors']:
            return player_move
        print("Wrong choice, try again.")

def get_computer_move():
    # Wylosuj ruch komputera
    computer_move = random.choice(['paper', 'rock', 'scissors'])
    return computer_move

def get_round_result(player_move, computer_move):
    # Sprawdź wynik rundy
    if player_move == computer_move:
        return "Tie"
    elif player_move == 'paper' and computer_move == 'rock':
        return "you won!"
    elif player_move == 'rock' and computer_move == 'scissors':
        return "you won!"
    elif player_move == 'scissors' and computer_move == 'paper':
        return "you won!"
    else:
        return "you lose!"

def update_score(score, result):
    # Zaktualizuj punktację
    if result == "you won!":
        score[0] += 1
    elif result == "you lose!":
        score[1] += 1

def print_score(score):
    # Wyświetl aktualny stan punktacji
    print(f"You: {score[0]}   Computer: {score[1]}")

def play_rock_paper_scissors():
    # Zacznij grę
    score = [0, 0]
    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()
        result = get_round_result(player_move, computer_move)
        update_score(score, result)
        print(result)
        print_score(score)
        if input("Press Enter to continue, or write 'q', to end the game: ") == 'q':
            break

play_rock_paper_scissors()
