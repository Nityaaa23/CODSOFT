# ROCK-PAPER-SCISSORS-GAME

import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_round():
    """Play a single round of the game."""
    # Get user choice
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            break
        print("Invalid choice. Please choose rock, paper, or scissors.")

    # Get computer choice
    computer_choice = get_computer_choice()
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display the result
    print(f"\nUser choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")
    
    return result

def main():
    """Main function to handle the game loop and score tracking."""
    user_score = 0
    computer_score = 0

    while True:
        # Play a round and update scores
        result = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        # Display scores
        print(f"\nScore - User: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
