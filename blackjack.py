import random
def get_choice():
    options = list(range(12))
    player_choice = print(f"Enter your card of choice from {options}: ")
    device_choice = random.choice(options)
    return options
    
def card_draw(player):
    print("Do you want to add a card or stay?")
    list_choice = ["Pull","Stay"]
    if player == "Pull":
        get_choice()
        