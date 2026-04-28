import random
def get_choice():
    player_choice=input("enter a choice:rock,paper,scissor:")
    option=["rock","paper","scissor"]
    computer_choice=random.choice(option)
    choice=get_choice()
    return choice