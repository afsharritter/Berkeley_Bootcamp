# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csv_path = os.path.join('..','Resources','netflix_ratings.csv')

# Open the CSV
with open(csv_path) as csv_data:
   
# Loop through looking for the video
    csv_reader = csv.reader(csv_data, delimeter=',')
    # print(csv_reader) not necessary


    for row in csv_reader:
        if row[0] == video:
            print(f"the video {row[0]} has a rating of {row[5]}")

