"""
Write a program able to play the "Guess the number" - game,
where the number to be guessed is randomly chosen between 1 and 20.
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random

print("Hello! What is your name?")

name = input()

print("Well,", name, "I am thinking of a number between 1 and 20.")

rnd = random.randrange(1, 20)

print("Take a guess.")

a = int(input())

if a > rnd:
    print("too high")
elif a < rnd:
    print("too low")
if a == rnd:
    print("Good job, KBTU! You guessed my number in 1 guesses!")
else:
    while a != rnd:
        cnt = 2
        print("Take a guess.")
        a = int(input())
        if a == rnd:
            print("Good job, KBTU! You guessed my number in", cnt, " guesses!")
        elif a > rnd:
            print("too high")
        else:
            print("too low")
        cnt += 1

