user_input = input("Enter a list of number: ")

split_number = user_input.split()

numbers = []

for i in split_number:
    parsed_number = int(i)

    numbers.append(parsed_number)

print(f"The maximum number within the list = {max(numbers)} and minimum within the list = {min(numbers)}.")



