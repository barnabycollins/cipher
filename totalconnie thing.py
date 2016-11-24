cipher = input("Cipher:\n")
number = int(input("\nWhat number would you like to test up to?\n--> "))
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
results = []
splits = []
freqs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# cycle through all the numbers up to the maximum value
for i in range(number):
    results.append([])
    splits.append([])
    if i != 0 and len(cipher) % (i) == 0:
            
        # create sublist entries for each split
        k = 0
        for k in range(i):
            splits[i].append("")

        # fill those sublist entries
        k = 0
        for letter in cipher:
            splits[i][k%i] = splits[i][k%i] + letter
            k+=1

        # find totalconnie for each sublist entry
        for l in range(len(splits[i])):
            results[i].append(0)
            totalconnie = 0
            for letter in alphabet:
                freqs[alphabet.index(letter)] = splits[i][l].count(letter)
                totalconnie = totalconnie + (freqs[alphabet.index(letter)] * freqs[alphabet.index(letter)] - freqs[alphabet.index(letter)])

            results[i][l] = round(totalconnie/(len(splits[i][l]) * len(splits[i][l]) - len(splits[i][l])), 5)
    else:
        results[i].append("Invalid")

    print(str(i) + ": " + str(results[i]))
