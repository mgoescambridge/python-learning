print("*** Find total lines ***")

txt_file = input("Enter file name: ")
read_file = open(txt_file, "r")

counter = 0

for i in read_file:
    counter += 1
read_file.close()

print(f"property => {read_file}")
print(f"Total lines: {counter}")

print("===== End of progam =====")