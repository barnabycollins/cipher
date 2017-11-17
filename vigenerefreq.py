cipher = input("Cipher:\n")
split = int(input("\nHow long is the keyword?\n--> "))
key = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
commonletters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
letters = {}
splits = []
sortedletters = []
plain = ""
finished = ""

# splitting the cipher up
for i in range(split):
    splits.append("")

i = 0
for letter in cipher:
    splits[i%split] = splits[i%split] + letter
    i+=1

# iterating over each split
for i in range(len(splits)):
    
    # making an array of letters in order of frequency for the current split
    key.append({})
    for letter in alphabet:
        letters[letter] = splits[i].count(letter)
    sortedletters.append(sorted(letters, key=letters.get, reverse=True))

    # generating a key
    j = 0
    for k in sortedletters[i]:
        key[i][k] = commonletters[j].upper()
        j += 1

    # using the key to decrypt each split and throw it into one massive string called plain
    for character in splits[i]:
        if(character in key[i]):
            plain = plain + key[i][character]

        else:
            plain = plain + character

    
for j in range(int(len(cipher)/split)):
    for i in range(split):
        finished = finished + plain[int(len(cipher)/split)*i + j]

# accounting for remainder characters
for j in range(len(cipher)%split):
    finished = finished + key[i][splits[j][-1:]]

print(finished)
