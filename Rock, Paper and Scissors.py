import random

while True:
    user_input = ""
    second_player_input = ""
    computer_action =""
    computer = input("\nYou want to play with copmuter(y/n)?: ")
    if (computer != 'y'):
        play_with_second_Player = True
        play_with_computer = False
    else:
        play_with_computer = True
        play_with_second_Player = False

    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    
    if (play_with_second_Player):
        second_player_input = input("Enter a second player choice (rock, paper, scissors): ").lower()
        print(f"\n player 1 chose {user_action}, player 2 chose {second_player_input}.\n")
        if user_action == second_player_input:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if second_player_input == "scissors":
                print("Rock beats scissors! Player 1 wins!")
            else:
                print("Paper beats rock! player 2 wins!")
        elif user_action == "paper":
            if second_player_input == "rock":
                print("Paper beats rock! Player 1 wins!")
            else:
                print("Scissors beats paper! player 2 wins!")
        elif user_action == "scissors":
            if second_player_input == "paper":
                print("Scissors beats paper! Player 1 wins!")
            else:
                print("Rock beats scissors! player 2 wins!")
        else:
            print("\n Please provide valid inputs!")
    else:
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock beats scissors! You win!")
            else:
                print("Paper beats rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper beats rock! You win!")
            else:
                print("Scissors beats paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors beats paper! You win!")
            else:
                print("Rock beats scissors! You lose.")
        else:
            print("\n Please provide valid inputs!")
        
    play_again = input("Play again? (y/n): ")
    if (play_again.lower() != "y"):
        break
    
    
        
