user = raw_input("chose ROCK, PAPER, SCISSORS: ")
from random import randint
ai = randint(1, 3)
if ai == 1:
    ai = "ROCK"

if ai == 2:
    ai = "PAPER"

if ai == 3:
    ai = "SCISSORS"

if ai == user:
    print(ai + ", DRAW")

if ai == "ROCK":
    if user == "SCISSORS":
        print("ROCK, YOU LOSE")

if ai == "PAPER":
    if user == "ROCK":
        print("PAPER, YOU LOSE")

if ai == "SCISSORS":
    if user == "PAPER":
        print("SCISSORS, YOU LOSE")

if ai == "ROCK":
    if user == "PAPER":
        print("ROCK, YOU WIN")

if ai == "PAPER":
    if user == "SCISSORS":
        print("PAPER, YOU WIN")

if ai == "SCISSORS":
    if user == "ROCK":
        print("SCISSORS, YOU WIN")