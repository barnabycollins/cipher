cipher = input("Cipher:\n")
dictionary = {}

for i in range(len(cipher) - 3):
    text = cipher[i] + cipher[i+1] + cipher[i+2] + cipher[i+3]
    if text in dictionary:
        dictionary[text] += 1

    else:
        dictionary[text] = 1
        
sorteddict = sorted(dictionary, key=dictionary.get, reverse=False)
for i in sorteddict:
    print(i + ": " + str(dictionary[i]))
