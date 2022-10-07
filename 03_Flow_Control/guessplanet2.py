# name: str = "zortan"

# guess = input("Louis Says: Can you guess my planet? >>> ")
# print(guess)

current_guess = False
planet = "zortan"

guess = input("Louis Says: Can you guess my planet? >>> ")
# While Loop

while current_guess is not True:
    if guess == planet:
        current_guess = True
        print("You got it brahhhh, Welcome")
    else:
        current_guess = True
        print("You failed brahhhhh")