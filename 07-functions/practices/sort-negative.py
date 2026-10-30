print("*** Sort avoid negative number ***")

def sort_avoid_negative(arr):
    non_negative = []
    for n in arr:
        if n >= 0:
            non_negative.append(n)

    sorted_list = sorted(non_negative)

    result = []
    counter = 0

    for n in arr:
        if n < 0:
            result.append(n)
        else:
            next_number = sorted_list[counter]
            result.append(next_number)
            counter += 1

    return result

user_input = input("Enter Input: ").split()

numbers = []

for i in user_input:
    i = int(i)
    numbers.append(i)


normal_sort = sorted(numbers)
print(f"Normal sort: \n {normal_sort}")
print(f"Avoid negative number sort: \n {sort_avoid_negative(numbers)}")


print("===== End of program =====")

