import datetime

current_time = datetime.datetime.now()  
#print(current_time)
print(current_time.strftime("%m/%d/%y"))

print(current_time.strftime("%B, %d, %Y"))

print(current_time.strftime("%B, %d, %Y %I:%M %p"))

import random

random_number = random.randrange(100)

correct_guess = False

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
try:
    number = int(user_input)
    if number == random_number:
        correct_guess = True
    elif number > random_number:
        print("Your guess is too high!")
    elif number < random_number:
        print ("Your guess is too low!")
    except:
        print("Please enter a number.")
print("You guessed the right number!")
