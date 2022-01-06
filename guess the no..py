#python program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.
#Following program gives user a hint to guess the number. Every each time the user guesses wrong, he/she gets another clue,
#by each another chance, his/her score get reduced.Clue can be multiples, divisible, greater or smaller, or a combination of all.

import random

print("Welcome to the number game. A random number will be generated and you can guess which one it is.")
print("You got five tries.")

number = random.randrange(1, 100)
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != number and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("Enter a guess: "))
        guess_count += 1
        if guess < number:
            print("Your guess is too low. Please try again.")
        elif guess > number:
            print("Your guess is too high. Please try again.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses.You loose!")
else:
    print("Your guess is correct.You Won!")