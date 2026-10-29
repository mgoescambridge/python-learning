# Project 1: Computer Guessing Game (Indefinite Loops)
#
# The computer picks a secret number from 1 to 100, then tries to guess it
# by itself, with a maximum of 5 guesses. After each guess, it prints a hint.
#
# Allowed: while, if/elif/else, comparisons, random.randint, print
# Not allowed: for, break, while True, lists, def, try/except

import random
secret = random.randint(1, 100)    # random whole number, 1 and 100 both included

guesses = 5    # Initialisation: number of guesses remaining
guess = 0      # Initialisation: 0 can never be the secret, so the test below
               # is True at the start and the loop is guaranteed to begin

# Test: keep going only while BOTH are True:
#   1. there are guesses left
#   2. the last guess was wrong
# If either becomes False, the loop ends.
while guesses > 0 and guess != secret:
    # Step 1: make a new guess FIRST...
    guess = random.randint(1, 100)
    print(guess)

    # Step 2: ...then check it immediately
    if guess == secret:
        print("Congrats!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

    guesses = guesses - 1    # Update: one fewer guess left (moves towards guesses == 0)

# After the loop: find out WHY it stopped.
# If the last guess is still wrong, the loop must have ended by running out.
if guess != secret:
    print(f"You're out of guesses! The number was {secret}")


# Lessons Learned
#
# 1. Order matters inside a loop: GUESS first, then CHECK.
#    Checking first meant the first check was on the fake 0, and the last
#    guess was never checked at all.
#
# 2. A loop can have more than one stopping reason. Combine conditions with
#    "and": the loop continues only while ALL of them are True.
#
# 3. The initial value can be chosen on purpose to make the loop start
#    (guess = 0 makes "guess != secret" True on the first test).
#
# 4. The check "guesses == 0" can never be True INSIDE the loop, because the
#    test only lets the body run while guesses > 0. Checks about how the loop
#    ended belong AFTER the loop.
#
# 5. Testing tip: temporarily print(secret) or set a fixed secret
#    (e.g. secret = 37) to test each case. Remove it when finished.
#
# 6. Changing numbers (5 → 6, > 0 → > 1) to "fix" a bug usually hides it
#    instead of fixing it. Trace the loop to find the real cause.