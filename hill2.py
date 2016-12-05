import numpy

ciphernums = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cipher = input("Cipher:\n")
guesser = input("\n4-letter guessword:\n--> ")
keywords = ["JAMELIA",
            "MARTIN",
            "CHARLIE",
            "CITADELLE",
            "PDSSYNDICATE",
            "DYNAMIX"]
ciphermatlist = []
finishedmatlist = []
finished = ""

# generate a matrix for the guess
guessernums = []
for i in guesser:
    guessernums.append(str(alphabet.index(i)))
guessermat = numpy.matrix(guessernums[0] + " " + guessernums[1] + " ; " + guessernums[2] + " " + guessernums[3])


# looping through the cipher to try the guess in each possible location
for i in range(len(cipher) - len(guesser)):
    foundwords = []

    # generating a matrix for the current section of cipher
    for j in range(len(guesser)):
        ciphernums.append(alphabet.index(cipher[j+i]))
    ciphermat = numpy.matrix(ciphernums[0] + " " + ciphernums[1] + " ; " + ciphernums[2] + " " + ciphernums[3])

    # generate the key matrix
    '''
    I NEED TO WORK OUT HOW TO DO THIS
    HALP
    '''

    # generate a matrix for each pair of letters
    for j in range(len(cipher)/2):
        ciphermatlist.append(numpy.matrix(str(alphabet.index(cipher[i*2])) + " ; " + str(alphabet.index(cipher(i*2+1)))))

    # multiply these matrices by those of the guesses
    for j in ciphermatlist:
        finishedmatlist.append(numpy.mod(numpy.dot(guessermat, j), 26))

    # generate a string from these multiplied matrices
    for j in finishedmatlist:
        finished.append(alphabet[j.item(0,0)])
        finished.append(alphabet[j.item(0,1)])

    # look for keywords in this string
    for j in keywords:
        if j in finished:
            output = True
            foundwords.append(j)
            
    # print the string if it has keywords in it
    if len(foundwords) > 0:
        print("Found " + str(foundwords) + " in:\n" + finished)
