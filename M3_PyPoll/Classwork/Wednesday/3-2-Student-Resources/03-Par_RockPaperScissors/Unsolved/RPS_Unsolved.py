# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == 'r' and user_choice == 'p':
    print("You win! You chose Paper. Paper covers rock.")
elif computer_choice == 'r' and user_choice == 's':
    print("You lose! You chose Scissors. Rock smashes scissors.")
elif computer_choice == 'r' and user_choice == 'r':
    print("It's a Draw! You both chose Rock. Try again.")    
elif computer_choice == 'p' and user_choice == 'p':
    print("It's a Draw! You both chose Paper. Try again.")    
elif computer_choice == 'p' and user_choice == 's':
    print("You win! You chose Scissors. Scissor cuts paper.")
elif computer_choice == 'p' and user_choice == 'r':
    print("You lose! You chose Rock. Paper covers rock.")
elif computer_choice == 's' and user_choice == 'p':
    print("You lose! You chose Paper. Scissor cuts paper.")
elif computer_choice == 's' and user_choice == 's':
    print("You lose! You chose Scissors. Scissor cuts paper.")
elif computer_choice == 's' and user_choice == 'r':
    print("You lose! You chose Rock. Paper covers rock.")




# orrrrr

if ((computer_choice == 'r' and user_choice == 'p') or (computer_choice == 's' and user_choice == 'r') or (computer_choice == 'p' and user_choice == 's')):
    print("You won")
elif (computer_choice == 'p' and user_choice == 'r') or (computer_choice == 'r' and user_choice == 's') or (computer_choice == 's' and user_choice == 'p'):
    print("You lost")
else:
    "it's a draw!"

# orrrrrrrrr

if computer_choice == user_choice:
    print("It's a Draw")
elif (computer_choice == 'p' and user_choice == 'r') or (computer_choice == 'r' and user_choice == 's') or (computer_choice == 's' and user_choice == 'p'):
    print("You lost")
else:
    print("you wint!") 