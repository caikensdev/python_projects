import random

def roll (sides=6):
    num_rolled = random.randint (1,sides)
    return num_rolled

def main():
    user_input = input("Ready to roll ? ENTER = Roll. Q = Quit.")
    if user_input.lower() != "q":
        num_rolled = roll(6)
        print("you rolled a ", num_rolled)
        return
    else:
        print("Thanks for playing the game!")
        return
main()