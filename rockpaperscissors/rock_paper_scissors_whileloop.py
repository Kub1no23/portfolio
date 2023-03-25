
import random

player_wins = 0
ai_wins = 0

rpc = ["rock", "paper", "scissors"]
nums = [0]

for num in nums: #tohle tu je k ničemu
    enter = input("Do you want to enter the game yes/no: ").lower()
    if enter == "yes":
        enter == True
    elif enter == "no":
        print("Oki")
        break
    else:
        print("Invalid input.")
        break
    while enter:
        random_number = random.randint(0, 2)
        ai_pick = rpc[random_number]
        player_input1 = input("Choose between rock/paper/scissors or Q to quit: ").lower()
        if player_input1 == "q":
            print("You have quit the game.")
            break
        elif player_input1 not in rpc:
            continue
        print("The opponent picked " + ai_pick + ".")
        if player_input1 == "rock" and ai_pick == "scissors":
            print("You've won!")
            player_wins += 1
            print("Your score is " + str(player_wins) + ".")
        elif player_input1 == "paper" and ai_pick == "rock":
            print("You've won!")
            player_wins += 1
            print("Your score is " + str(player_wins) + ".")
        elif player_input1 == "scissors" and ai_pick == "paper":
            print("You've won!")
            player_wins += 1
            print("Your score is " + str(player_wins) + ".")
        elif player_input1 == ai_pick:
            print("Tie, nobody wins!")
        else:
            print("You've lost!")
            ai_wins += 1
            print("Your opponent's score is " + str(ai_wins) + ".")