# Learn string manipulation and concatination
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)

# Using variables to calc the length
username = input("What is your name")
length = len(username)
print(length)
# All in one line, this will 1st complete 'input', 2ndly 'len', 3rdly 'print'
print(len(input("What is your name?")))
