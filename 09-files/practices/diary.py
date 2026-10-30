print("*** Diary ***")
text = input("Please enter one line of text: ")

opened_file = open(text, "a")
opened_file.write(text)
