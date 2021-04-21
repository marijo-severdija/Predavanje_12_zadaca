import random
import json
import datetime
from operator import itemgetter

def hard():
    print("Your guess is not correct...")

def easy(hint):
    print(f"Your guess is not correct... try something {hint}")


def best_scores():
    with open("guess_game.json", "r") as score_file:
        score_list = json.loads(score_file.read())

    best_score = sorted(score_list, key=itemgetter("attempts"))
    top_three = 0

    for score_dict in best_score:
        if top_three == 3:
            break
        else:
            print(f"player: {score_dict['player']},"
                  f" secret number: {score_dict['secret']},"
                  f" {score_dict['attempts']} attempts,"
                  f" date: {score_dict['date']},"
                  f" wrong guesses: {score_dict['wrong_guesses']}")
        top_three += 1


def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []

    with open("guess_game.json", "r") as score_file:
        score_list = json.loads(score_file.read())

    level = input("Choose game difficulty level (hard/easy): ")

    while True:
        guess = int(input(f"\nGuess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:

            score_list.append({"player": player,
                               "secret": secret,
                               "attempts": attempts,
                               "date": str(datetime.datetime.now()),
                               "wrong_guesses": wrong_guesses})

            with open("guess_game.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            hint = "smaller"
            if level.lower() == "hard":
                hard()
            else:
                easy(hint)
        elif guess < secret:
            hint = "bigger"
            if level.lower() == "hard":
                hard()
            else:
                easy(hint)

        wrong_guesses.append(guess)


player = input("Please enter your name: ")
play_game()
while True:
    selection = input(f"\nDo you want to play again (A), see best scores (B) or quit the game (C)?: ")
    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        best_scores()
    else:
        break
