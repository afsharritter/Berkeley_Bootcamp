# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Specify the file to write to the movie data.


# Set a variable to false to check if we found the video
found = False

# Open the NetFlix CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:

            # Set the variable created in Step 1 to confirm we have found the video
            found = True
            # specify file 
            output_path = os.path.join(".", "netflix_data.txt")
            # Open the file using "write" mode. Specify the variable to hold the contents
            with open(output_path, 'w') as outfile:
                
                # Create a variable to hold the title, rating level, and the movie rating inside parentheses.
               title, rating_level, user_rating = row[0], row[1], row[5]
                
                # Write the movie data to the text file.
                title_data = (
                    "\nTitle\tRating\tUser_Rating\n"       
                    f"\n{title}\t{rating_level}\t{user_rating}\n"
                )
                outfile.write(title_data)

                # Print the movie data to the console.
                print(title_data)

            # Stop at first results to avoid duplicates
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
