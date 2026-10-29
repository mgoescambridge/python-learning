# Indexing Method

Word = "Hello"

print(Word[-1]) # Output = 'o' because [-1] meaning the first order from the last 
print(Word[-2]) # Output = "l" becasue [-2] meaning the second order from the last
print(Word[-3]) # Output = "l" because [-3] meaning the third order from the last
print(Word[-4]) # Output = "e" because [-4] meaning the fourth order from the last
print(Word[-5]) # Output = "H" because [-5] meanign the fifth order from the last

# Reversing the index like in the example, the first letter to last will be [-1] and cannot be [0] because it's default to first letter from the start.

# Indexing from the default position to last

Word = "World"

print(Word[0]) # Output = 'W' because [0] because in Python started from 0 and so on...
print(Word[1])
print(Word[2])
print(Word[3])
print(Word[4])

# Combining all of these print statement will become 'World' but in extracted term.


# Slicing Method [start:stop:step] <--- Default format for Slicing Method

Word = "Hello"

# Let n = indexes, s = start, e = end, and z = number of step where [s, e, z]
# Mathematically defined as:

# s ≤ n < e for all z > 0 | Example: [0:5:1]

print(Word[0:5:1]) # --> Output = 'Hello' as it iterate from [0]{'H'} -> [5]{''}, with 1 step add per checking

print(Word[1:5:1])

print(Word[1:4:1])


# s ≥ n > e for all z < 0 | Example [5:0:-1] # Reversing String Method

print(Word[5:0:-1])
print(Word[4:1:-1])
print(Word[5::-2])


