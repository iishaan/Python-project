import random
the_number = random.randint(1,10)
guess = int(input("guss a number between 1 and 10: "))
while guess != the_number:
    if guess > the_number:
        print(guess,"was to high. try again.")
    if guess < the_number:
        print(guess,"was too low. try again.")
    guess = int(input("guess again: "))
print(guess,"was the right answer you win")