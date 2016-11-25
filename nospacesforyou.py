intake = input("Input:\n")
removalchar = input("\nWhich character would you like to remove?\n--> ")
cipher = ''
for letter in intake:
    if letter != removalchar:
        cipher = cipher + letter
print(cipher)
