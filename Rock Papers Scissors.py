import random

def get_choices():
    player_choice = input("Enter choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]

    # validate input
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        return get_choices()

    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}.")

    if player == computer:
        return "It's a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"

    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
