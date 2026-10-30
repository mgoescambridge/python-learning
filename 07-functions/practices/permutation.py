# Permutation is the order of arrangement where if two objects arranged differently but with same items inside are defined as 'permutation'
# Otherwise, if two of objects arranged differently without same items are defined as 'non-permutation'

print("*** Permutation ***")

def permutation(str1, str2):
    if len(str1) == len(str2):
        letters = list(str2)

        for i in str1:
            if i in letters:
                letters.remove(i)
            else:
                print("String 1 and String 2 are not permutation")
                return
        print("String 1 and String 2 are permutation.")
    else:
        print("String 1 and String 2 are not permutation.")



string = input("Enter two strings: ").split("/")
permutation(string[0], string[1])

print("===== End of program =====")



