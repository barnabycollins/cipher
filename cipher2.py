# BARNABY'S CIPHER SOLVER, V2.4
# 03/11/2016 DEVELOPED IN PYTHON 3.5.2

key = {}
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
commonletters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
letters = {}

print('Please paste the cipher without any breaks:')
cipher = input()
OG = cipher

# Letter frequency analysis
def charfreq(cipher, OG):
    print("\nAnalysing...\n")

    total = 0
    totalconnie = 0

    for letter in alphabet:
        letters[letter] = cipher.count(letter)

    sortedletters = sorted(letters, key=letters.get, reverse=True)

    for char in sortedletters:
        print(char + ": Frequency " + str(letters[char]) + " | n2-n " + str(letters[char]*letters[char]-letters[char]))
        total = total + letters[char]
        totalconnie = totalconnie + (letters[char]*letters[char]-letters[char])
    print("\nTotal: " + str(total) + ", TotalConnie: " + str(totalconnie/(total*total-total)))

    if(input("\nWould you like to attempt to decrypt the cipher using this data? (y/n)\n--> ") == "y"):
        print("\nAttempting decryption based on letter frequency...\n")

        j = 0
        for i in sortedletters:
            key[i] = commonletters[j].upper()
            j += 1

        plain = ''

        for character in cipher:
            if(character in key):
                plain = plain + key[character]

            else:
                plain = plain + character

        print(plain)
        print("\nKey: " + str(key))

    menu(plain, OG)


# Character removal
def charremove(cipher, OG):
    removalchar = input("\nWhich character would you like to remove?\n--> ")
    new = ""
    for letter in cipher:
        if letter == removalchar:
            pass
        else:
            new = new + letter

    print("Operation complete.")
    menu(new, OG)


# Character replacement
def charreplace(cipher, OG):
    if(len(key) == 0):
        keygen = input("\nKey is ungenerated. Here are your options:\n1:  Manually enter values\n2:  Generate parallel key\n3:  Return to menu\n--> ")
        if(keygen == "1"):
            i = 0
            for letter in alphabet:
                current = input('Please enter the plaintext of cipher ' + alphabet[i] + '.\n--> ')
                if current == '' or len(current) > 1:
                    if(input("Error: Invalid value entered.\nIs this intentional? (y/n)\n--> ") != "y"):
                        current = input('Please enter the plaintext of cipher ' + alphabet[i] + '.\n--> ')
                        key[letter] = current
                
                else:
                    key[letter] = current
                
                i = i + 1

        elif(keygen == "2"):
            for letter in alphabet:
                key[letter] = letter
            print("Generation complete.")

        else:
            print("Returning to menu...")
            menu(cipher, OG)

    else:
        if(input("\nWould you like to view the cipher? (y/n)\n--> ") == "y"):
            print(cipher)
            
        modify = "y"
        while modify == "y" or modify == "Y":
            modify = input("\nWould you like to modify the key? (Y/N)\n--> ")
            if modify == "y" or modify == "Y":
                keychange = input("\nWhich letter in the cipher should be changed?\n--> ")
                replacement = input("Which letter would you like to change it for?\n--> ")
                reversekey = dict(zip(key.values(),key.keys()))
                key[reversekey[keychange]] = replacement
                key[reversekey[replacement]] = keychange

                print("New key: " + str(key))
                print("Reprinting your altered cipher...")
                plain = ''
                for character in OG:
                    if(character in key):
                        plain = plain + key[character]

                    else:
                        plain = plain + character

                print(plain)
                cipher = plain

    menu(cipher, OG)


# Menu
def menu(cipher, OG):
    menu = input("\n============================MENU============================\nWhich function would you like to perform?\n1:  View the cipher and key in their current form\n2:  View the original cipher\n3:  Letter frequency analysis\n4:  Character Removal\n5:  Create or modify the key\n8:  Revert to the original cipher\n9:  Exit\n\n--> ")
    if(menu == "1"):
        print("Printing current cipher and key:\n" + cipher + "\nKey:\n" + str(key))
        menuredir(cipher, OG)
    elif(menu == "2"):
        print("Printing original cipher:\n" + OG)
        menuredir(cipher, OG)
    elif(menu == "3"):
        charfreq(cipher, OG)
    elif(menu == "4"):
        charremove(cipher, OG)
    elif(menu == "5"):
        charreplace(cipher, OG)
    elif(menu == "8"):
        cipher = OG
        menuredir(cipher, OG)
        print("Operation complete.")
    else:
        if(input("Are you sure you want to exit? (y/n)\n--> ") != "y"):
           menuredir(cipher, OG)

def menuredir(cipher, OG):
    menu(cipher, OG)

menu(cipher, OG)
