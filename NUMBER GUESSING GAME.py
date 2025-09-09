print("====================================".center(50))
print(" :)   NUMBER GUESSING GAME    (: ".center(50))
print("====================================".center(50))

import random
number = random.randint(10, 20)

attempts = 0
max_attempts = 5
guess = None

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter a guess between 10 and 20: "))
    attempts += 1
    
    if guess == number:
        print("Your guess is correct!")
        break
    elif guess > number:
        print("Your guess is too high...")
    else:
        print("Your guess is too low...")

# If the loop ends without correct guess
if guess != number:
    print(" Sorry, you've used all your attempts.")
    print(f"The secret number was: {number}")
else:
    print(f"You guessed it in {attempts} tries!")
