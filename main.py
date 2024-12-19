# Imports

import pyperclip as clipboard




#Step1 : Create a dictionary that contains all the alphabetic codes

dictionary = {}

with open("alphabets") as file:
    codes = file.readlines()
    for line in codes:
        characters = line.split(sep="\t")
        dictionary[characters[0]] = characters[1].strip("\n")
dictionary[" "] = "/"


# Step 2 : Make Selection

print("\n\t\t\t\t\t\tTEXT TO MORSE CODE\n")
choice = int(input("Enter 0 to encode or 1 to decode: "))

# Step 3: Encode
if choice == 0:
    inp = input("Please type below to convert:\n\t ").upper()
    encoded = []
    for character in inp:
        if character in dictionary:
            encoded.append(dictionary[character])
            encoded.append(" ")
    clipboard.copy("".join(encoded))
    print("\n The code is copied to your clipboard")

#Step 3: Decode
else:
    inp = input("Paste the code below:\n\t ")

    # Seperating codes from the text
    codes = []
    temp = []
    for character in inp:
        if character != " ":
            temp.append(character)
        else:
            codes.append("".join(temp))
            temp = []

    # Decoding

    keys = list(dictionary.keys())
    values = list(dictionary.values())
    decoded = []
    for code in codes:
        position = values.index(code)
        decoded.append(keys[position])
    print("".join(decoded))


