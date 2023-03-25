import random

rpc = ["rock", "paper", "scissors"]

random_number = random.randint(0, 2)
ai_pick = rpc[random_number]

player_input1 = input("Do wou wish to enter the game Yes/No: ").lower()
if player_input1 == "yes":
    player_input2 = input("Choose between rock/paper/scissors or Q to quit the game: ").lower()
    if player_input2 == "rock" and ai_pick == "scissors":
        print("You have won!")
    elif player_input2 == "paper" and ai_pick == "rock":
        print("You have won!")
    elif player_input2 == "scissors" and ai_pick == "paper":
        print("You have won!")
    elif player_input2 == "scissors" and ai_pick == "rock":
        print("You have lost!")
    elif player_input2 == "rock" and ai_pick == "paper":
        print("You have lost!")
    elif player_input2 == "paper" and ai_pick == "scissors":
        print("You have lost!")
    elif player_input2 == ai_pick:
        print("Tie, nobody wins!")
    elif player_input2 == "q":
        print("You have quit the game.")
        quit()
    elif player_input2 != "rock" or "paper" or "scissor" or "q":
        print("Invalid input! You've been disconnected.")
elif player_input1 == "no":
    print("ok")
else:
    print("Invalid input!")
