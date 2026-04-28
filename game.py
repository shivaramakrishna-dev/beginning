import random
def get_choice():
    player_choice=input("enter a choice(rock,paper,scissor):")
    option=["rock","paper","scissor"]
    computer_choice=random.choice(option)
    choice={"player":player_choice,"computer":computer_choice}
    return choice
def check_win(player,computer):
    print(f"you choose:{player},computer choose:{computer}")
    if player==computer:
     return "it's a tie!"
    elif player == "rock":
       if computer == "scissor":
          return "rock smash scissor!you win"
       else:
          return "paper wrap rock!you lose"
    elif player == 'paper':
       if computer =="rock":
          return "paper wrap rock!you win"
       else:
          return "scissor cuts paper!you lose"
    elif player  == "scissor":
       if computer == "paper":
          return "scissor cut paper!you win"
       else:
          return "rock samsh scissor!you lose"
while True:
   choice=get_choice()
   result=check_win(choice["player"],choice["computer"])
   print(result)
   play_again=input("play again yes/no:")
   if play_again == "no":
      break