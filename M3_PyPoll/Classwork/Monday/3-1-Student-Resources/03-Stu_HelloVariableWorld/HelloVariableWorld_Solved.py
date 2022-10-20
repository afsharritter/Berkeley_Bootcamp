
name = "Justin"
country = "Canada"
years = 42
hourly_wage = 145
daily_wage = hourly_wage * 8
satisfied = False
print("Hello " + name)
print("You are from " + country)
print("You are " + str(years) + " years old")
print(f"You make: ${daily_wage}/hour")
print(f"True of False, You're satisfied, right? lol {satisfied}.")


# Create a variable called 'name' that holds a string
name = "Justin"

# Create a variable called 'country' that holds a string
country = "Canada"

# Create a variable called 'age' that holds an integer
years = 42

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 145

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Create a variable called 'satisfied' that holds a boolean
satisfied = False

# Print out "Hello <name>!"
print("Hello " + name)

# Print out what country the user entered
print("You are from " + country)

# Print out the user's age
print("You are " + str(years) + " years old")

# With an f-string, print out the daily wage that was calculated
print(f"You make: ${daily_wage}/hour")

# With an f-string, print out whether the users were satisfied
print(f"True of False, You're satisfied, right? lol {satisfied}.")
