import random
options = list(range(12))
def player_choice():
    player = print(f"Enter your card of choice from {options}: ")
    return player

def device_choice():
     device = random.choice(options)
     return device
    
def rounds():
    no_rounds = print("Enter no. of rounds: ")
    return no_rounds

def card_draw(player):
    print("Do you want to pull a card or stay? (Pull, Stay): ")
    no_rounds = rounds()
    for i in range(1, no_rounds+1):
        if player == "Pull":
            player_choice()
        else:
            continue

def sum_win(player_sum , device_sum):
    no_rounds = rounds()
    sum = random.choice(options)
    player = player_choice()
    device = device_choice()
    for i in range(1, no_rounds+1):
        player_sum = sum + player
        device_sum = sum + device
    if player_sum > 21 and device_sum<21:
        print("You lost!")
    elif device_sum > 21 and player_sum<21:
        print("You won!")
    elif player_sum > 21 and device_sum > 21 :
        print("Disqualification!")
    while(player_sum<21 and device_sum<21):
        if player_sum == device_sum:
            print("It's a Tie!")
        elif player_sum < device_sum:
            print("You lost!")
        else:
            print("You won!")

player = player_choice()
computer = device_choice()

round_number = rounds()
