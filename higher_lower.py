import random
import os

from higher_lower_art import logo, vs
from higher_lower_data import data


def clear():
    return os.system("clear")


def getChoice(exclude=-1):
    number = len(data)
    choice = exclude

    while choice == exclude:
        choice = random.randint(0, number - 1)

    return choice


def format_data(choice):
    return f"{data[choice_a]['name']}, a {data[choice_a]['description']}, from {data[choice_a]['country']}"


def show_output(choice_a, choice_b, score):
    clear()
    print(logo)

    if score > 0:
        print(f"Your're right! Current score: {score}.")

    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Against B: {format_data(choice_a)}")

    answer = ""
    while answer not in ["A", "B"]:
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    return answer


def is_correct(choice_a, choice_b, answer):
    if data[choice_a]["follower_count"] > data[choice_b]["follower_count"]:
        return answer == "A"
    else:
        return answer == "B"


high_score = 0

end_of_game = False

while not end_of_game:
    current_score = 0
    wrong_answer = False
    choice_a = getChoice()

    while not wrong_answer:
        choice_b = getChoice(choice_a)

        answer = show_output(choice_a, choice_b, current_score)

        if is_correct(choice_a, choice_b, answer):
            current_score += 1
            choice_a = choice_b
        else:
            wrong_answer = True

    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {current_score}.")

    if current_score > high_score:
        print("Congratulations. You've beaten the Highscore!")
        high_score = current_score
    else:
        print(f"Your highscore is {high_score}.")

    another_game = input("Another game? (y/n): ")
    if another_game != "y":
        end_of_game = True
