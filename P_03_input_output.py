# ask the user for their name
username = input("What is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print(f"Hi {username}, your favourite number is {fav_num}\n")
print(f"Half of your favourite number is {halve}.")
print(f"Your number, {fav_num}, doubled is {double}.")
print(f"{fav_num} squared is {square}.\n")
print(f"Have a great day!")

# Output the results of doubling, halving and squaring their favourite integer
