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

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_number = random.randint(1, 100)
guesses_left = 0
game_over = False

print(f"Pssst, the correct answer is {correct_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    guesses_left = 10
else:
    guesses_left = 5

while not game_over:
    print (f"You have {guesses_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == correct_number:
        print(f"You got it! The answer was {correct_number}.")
        game_over = True
    elif guess > correct_number:
        guesses_left -= 1
        print("Too high.")
    elif guess < correct_number:
        guesses_left -= 1
        print("Too low.")
        

    if guesses_left > 0 and not game_over:
        print("Guess again.")
    elif guesses_left == 0:
        print("You've run out of guesses, you lose.")
        game_over = True
