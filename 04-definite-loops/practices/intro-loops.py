# Introduction to Definite Loops

# A definite loop (for loop) runs a KNOWN number of times:
# once for each item in a sequence (a range, a string, a list, ...).
#
# Indefinite vs. Definite:
# ↳ while loop (indefinite) - Repeats while a condition is True. We don't know
#                             in advance how many times it will run.
# ↳ for loop (definite)     - Repeats once per item. The number of repetitions
#                             is known before the loop starts.
#
# Initialise, Test, Update in a for loop:
# The same three principles still apply, but Python handles them automatically:
# ↳ Initialise - The loop variable starts at the first value (start of range).
# ↳ Test       - The loop continues while there are values left in the range.
# ↳ Update     - The loop variable moves to the next value automatically (by step).
# Because Python does the update for us, a for loop over a range can never
# become an infinite loop by forgetting the update.


# range(start, stop, step)
# ↳ start - First value, INCLUDED (default 0)
# ↳ stop  - The loop stops BEFORE this value, NOT included
# ↳ step  - How much to add each time (default 1, can be negative)
#
# Rule: range(s, e) gives every integer n with  s <= n < e   (half-open interval [s, e))
#       Number of values = e - s
#       With a negative step, the rule flips:  s >= n > e
#
# range(5)          → 0, 1, 2, 3, 4
# range(1, 6)       → 1, 2, 3, 4, 5
# range(0, 10, 2)   → 0, 2, 4, 6, 8
# range(5, 0, -1)   → 5, 4, 3, 2, 1
#
# Common trap: to include the end number, add 1 to stop.
#              1 to 10 inclusive → range(1, 11)
#
# Connection: slicing uses the same rule.
#             lst[2:5] gives the elements at indices 2, 3, 4 (same as range(2, 5)).


# Countdown | Example:

for i in range(5, 0, -1):   # i takes the values 5, 4, 3, 2, 1
    print(i)
print("Blastoff!")          # After the loop (no indentation), so it runs once at the end


# Same countdown with a while loop, for comparison:
#
# i = 5                 # Initialise (done by hand)
# while i >= 1:         # Test (done by hand)
#     print(i)
#     i = i - 1         # Update (done by hand)
# print("Blastoff!")
#
# The for loop is shorter because range() handles all three parts.


# Looping over other sequences:
#
# for letter in "hi":
#     print(letter)      # h, then i
#
# for x in [3, 7, 2]:
#     print(x)           # 3, then 7, then 2
