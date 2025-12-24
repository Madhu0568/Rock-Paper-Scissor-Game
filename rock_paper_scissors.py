import random

print("=== Rock Paper Scissors ===")
print("Type: rock, paper, or scissors")
print("Type: quit to exit\n")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Your choice: ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice. Try again.\n")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("Result: Tie\n")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("Result: You win!\n")
    else:
        print("Result: You lose!\n")
