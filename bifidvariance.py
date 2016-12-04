import pycipher

cipher = input("Cipher:\n")
maxperiod = int(input("\nWhat period would you like to test up to?\n--> "))
bigrams = []
variances = []
print("\nPeriod  Variance")

# loop for each possible period up to and including the entered limit
for i in range(maxperiod+1):
    bigrams.append({})
    totalbigrams = 0
    bigramavg = 0.0
    bigramvar = 0.0
    
    # loop through the cipher and count the occurrence of each bigram
    for j in range(len(cipher)-(i+1)):
        currentbig = cipher[j] + cipher[j+i+1]
        if currentbig in bigrams[i]:
            bigrams[i][currentbig] += 1
        else:
            bigrams[i][currentbig] = 1

    # get the average bigram occurrence
    for j in bigrams[i].keys():
        totalbigrams += bigrams[i][j]
    bigramavg = totalbigrams / len(bigrams[i])

    # find the variance of the bigram occurrences
    for j in bigrams[i].keys():
        totalbigrams += (bigrams[i][j] - bigramavg)**2
    bigramvar = totalbigrams / len(bigrams[i])

    # print a graph showing the variances of each period
    print(str(i+1) + ": " + " " * (6 - len(str(i+1))) + "#" * int(round(4*bigramvar, 0)))
    variances.append(round(bigramvar, 5))

print("Each # signifies 0.25\n\nRaw values:\n" + str(variances))
