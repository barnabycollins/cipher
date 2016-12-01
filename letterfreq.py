key = {}
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
commonletters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
letters = {}
cipher = input("Cipher:\n")

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
