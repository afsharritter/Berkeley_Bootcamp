# Initial variable to track game play
user_play = "y"
marker = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_loop = int(input("How many numbers would you like to loop through?"))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(marker, (user_loop + 1) + marker):

        # Print each number in the range
        print(x)       
        marker += (user_loop + 1)
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
    # bonus
    # how to make it so that the next chain begins at the beginning 
    # while user_play == 'y':
    #     if user_play == 'y':
    #         user_loop = int(input("How many more numbers do you want to loop through?"))

    #     for numbers in range(user_loop + 1):
    #         marker += 1
    #         print(marker)





