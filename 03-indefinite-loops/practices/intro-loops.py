# Introduction to Indefinite Loops

# An indefinite loop (while loop) runs while a condition is True.
# We don't know in advance how many times it will run, but it should stop eventually.
#
# Indefinite vs. Infinite:
# ↳ Indefinite loop - The number of repetitions isn't known in advance, but the loop DOES stop.
# ↳ Infinite loop   - The loop NEVER stops (a bug!). Press Ctrl + C to stop the program.
#
# A while loop uses three principles to work properly:
# ↳ Initialise - Give the loop variable a starting value before the loop.
#                It can be a counter, but also any value the test depends on (e.g. user input).
# ↳ Test       - A conditional expression checked before every repetition.
#                If True, the loop body runs; if False, the loop ends.
# ↳ Update     - Change the loop variable inside the loop so the test eventually becomes False.
#                Forgetting this causes an infinite loop.


# Counting to 5 | Example:

i = 1           # <-- Initialise the loop variable

while i <= 5:   # <-- Test the condition
    print(i)
    i = i + 1   # <-- Update (i increases towards 6, which makes the test False)


# Countdown | Example:

i = 5           # <-- Initialise the loop variable

while i >= 1:   # <-- Test the condition
    print(i)
    i = i - 1   # <-- Update (i decreases towards 0, which makes the test False)

print("Lift off!")