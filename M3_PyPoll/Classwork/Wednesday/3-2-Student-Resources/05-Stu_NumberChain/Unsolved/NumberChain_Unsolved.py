# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_loop = int(input("How many numbers would you like to loop through?"))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for numbers in range(user_loop + 1):

        # Print each number in the range
        print(numbers)       

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")

    # bonus
    # how to make it so that the next chain begins at the beginning 








