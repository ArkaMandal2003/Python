import random


def greeting():
    return "Hi, Let's play rock , paper, scissors" 

print(greeting())

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors); ")
    options = ["rock", "paper", "scissors"]
    device_choice = random.choice(options)
    choices={"player": player_choice, "computer":device_choice}
    return choices

def check_win(player, device):
    print(f"you chose: {player}, computer chose: {device}")
    if player == device:
        return "It's a tie"
    elif player == "rock" :
        if device =="scissors":
            return "you win!"
        else:
            return "computer wins!"
    elif player == "paper":
        if device =="scissors":
            return "computer wins!"
        else:
            return "you win!" 
    else:
        if device =="paper":
            return "you win!"
        else:
            return "computer wins!"


choices = get_choices()
result = check_win(choices["player"], choices["player"])
print(result)
     