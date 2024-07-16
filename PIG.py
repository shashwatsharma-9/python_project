import random

def roll():
    min_Value=1
    max_value=6
    roll=random.randint(min_Value,max_value)

    return roll

while True:

    players=input("Enter the numbers of Players(1-4): \n")
    if players.isdigit():
        players=int(players)
        if 2<= players<= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_Score=50
player_Scores=[0 for _ in range(players)]
# jitne players honge utni bar 0 aa jayega LIST COMPRIHENSION

while max(player_Scores)<max_Score:
    for player_idx in range(players):
        print("\n Player",player_idx+1,"turn has just stareted!\n")
        current_Score=0

        while True:
            shoul_roll=input("Would you like to roll (y)? \n")
            if shoul_roll.lower()!="y":
                break
            # agr y print nahi kra to roll ho jayega dice 

            value=roll()
            if value == 1:
                print("You rolled 1! Turn done!")
                break

            else:
                print("You rolled a:",value)
                current_Score+=value
        
            print("Your score is:",current_Score)
        player_Scores[player_idx]+= current_Score
        # jo bhi player hai uska indiviadual score aa jayega
        print("Your total score is:",player_Scores[player_idx])
