# Students: ranste07, Gorbra14

import random
n = random.randint(1,100)

guessed = False

while (not guessed):
        guess = raw_input("Enter a guess: ")
        guess = int(guess)
        # Fill in the rest!
        if n == guess:
            guessed = True

        #tell the user if their guess is too high or too low
        if (guess > n):
            print 'Too High!'
        elif (guess < n):
            print 'Too Low!'
        else:
            print 'You are awesome, amazing, and good at life!'
        continue
