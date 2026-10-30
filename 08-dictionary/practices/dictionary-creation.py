print(" *** Creating dictionary ***")
 
user_input = input("Enter text: ").split()
 
result = {}
 
for i in range(1, len(user_input) // 2 + 1):
    key_position = (2 * i) - 2 # Key-Even position
    value_position = (2 * i) - 1 # Value-Odd position
 
    result[user_input[key_position]] = user_input[value_position]
 
print(result)

print("===== End of program =====")
 
    # Loop through user_input and then pick up the index using (2 * ) - 2 to find where the key for dictionary are.
 
    # 2 * 1 - 2 = 0
    # 2 * 2 - 2 = 2
    # 2 * 3 - 2 = 4
 
    # [0*, 1, 2*, 3, 4*, 5, 6*]
 
    # Expected outcome:
    # user_input = a 2 b 3
    # result = 'a': '2', 'b': '3'