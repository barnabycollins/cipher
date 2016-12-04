import pycipher
import random

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
best = 0

# randomly generate a key
for i in range(25):
    genrand = random.randint(0, 24)
    while genrand > len(genlist):
        genrand = random.randint(0, 24)
    genlist.insert(alphabet[i], genrand)
    
for i in genlist:
    key.append(i)

# piss around until we get something nice
for i in range(cycles):
    plain = pycipher.Bifid(key, period).decipher(cipher)
    fitness = ns.ngram_score("english_quadgrams.txt")
    if fitness.score(plain) > best:




