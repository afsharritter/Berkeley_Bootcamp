# @TODO: Your code here
hobbybook = dict()
hobbybook = {
    "name": "Keegan",
    "age": 27,
    "hobbies": ["complaining", "watching TV", "baking", "judging others"],
    "wakeup_times": {
        "Sunday": 9,
        "Monday": 6,
        "Tuesday": 8,
        "Wednesday": 6,
        "Thursday": 7,
        "Friday": 8,
        "Saturday": 9
    }
}

print(f"my pet is named {hobbybook['name']} and he is {hobbybook['age']} years old.")
print(f"my pet {hobbybook['name']} has {len(hobbybook['hobbies'])} hobbies")
print(f"my pet {hobbybook['name']}'s favorite hobby is {hobbybook['hobbies'][1]}.")
print(f"my pet {hobbybook['name']} wakes up at {hobbybook['wakeup_times']['Saturday']} AM on Saturdays")