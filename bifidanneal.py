import pycipher
import random
import ngram_score as ns
import math

'''

WARNING
-------
WHEN MAINTAINING THIS CODE, KEEP IN MIND THAT
ALL VALUES BASED OFF THE LENGTH OF THE ALPHABET MUST BE
REDUCED BY ONE AS J IS OMITTED

'''

cipher = input("Cipher:\n")
period = int(input("Period:\n--> "))
cycles = int(input("Number of cycles:\n--> "))
alphabet = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
genlist = []
best = -999999
fitness = ns.ngram_score("english_quadgrams.txt")
parent = ''
keywords = ["JAMELIA",
            "MARTIN",
            "CHARLIE",
            "TRINITY",
            "CITADELLE",
            "PDSSYNDICATE",
            "DYNAMIX"]

# randomly generate a key
for i in range(25):
    genrand = random.randint(0, 24)
    while genrand > len(genlist):
        genrand = random.randint(0, 24)
    genlist.insert(genrand, alphabet[i])
    
for i in genlist:
    parent = parent +i
child = parent

print("Working...")
# piss around until we get something nice
for i in range(cycles):
    keywordsfound = []

    # logic for testing the fitness of the key
    plain = pycipher.Bifid(child, period).decipher(cipher)
    goodness = fitness.score(plain)
    if goodness <= best:
        if random.random() < math.e**((goodness - best)/(10-(i/cycles)*10)):
            parent = child

    else:
        parent = child
        best = goodness
    
    # check the plaintext for keywords and print if it finds it
    for j in keywords:
        if j in plain:
            keywordsfound.append(j)
    if len(keywordsfound) >= 1:
        print(str(keywordsfound) + " found in:\n" + plain + "\nWith key:\n" + child)

    # randomly select the key positions to swap
    charpos = random.randint(0, len(child))
    charpos2 = random.randint(0, len(child))
    while charpos2 == charpos:
        charpos2 = random.randint(0, len(child))

    # swap the characters by making child into a list
    childlist = list(child)
    tempchar = childlist.pop(charpos-1)
    tempchar2 = childlist.pop(charpos2-2)
    childlist.insert(charpos2, tempchar)
    childlist.insert(charpos, tempchar2)

    # synchronise the childlist back into the child string
    child = ""
    for j in childlist:
        child = child + j

print(plain + "\nKey: " + child)
        
    
        




