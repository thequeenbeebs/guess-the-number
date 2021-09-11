#Number Guessing Game Objectives:

# Include an ASCII art logo. MAKE AS DOCSTRING
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# easy: 10 attempts
# hard: 5 attempts

# Write a To Do List
#  - create ascii art
#  - print welcome sign
#  - create variable that uses random to grab a random number 
#  - create variable that determines number of guesses left, based on choosing easy or hard
#  - create compare() function to compare with a guess
#  - input to choose difficulty

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
    elif guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    correct_number = random.randint(1, 100)

    print(f"Pssst, the correct answer is {correct_number}")
    turns = set_difficulty()
    guess = 0

    while guess != correct_number:
        print (f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, correct_number, turns)        

        if turns > 0 and guess != correct_number:
            print("Guess again.")
        elif turns == 0:
            print("You've run out of guesses, you lose.")
            return
game()
