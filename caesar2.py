alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
counts = {}
key = {}
curmax = 0
plain = ''

cipher = input("Cipher:\n").upper()
printnums = int(input("How many results do you want to output?\n--> "))

for i in alphabet:
    counts[i] = cipher.count(i)

counts = sorted(counts, key=counts.get, reverse=True)
for i in range(printnums):
    plain = ''
    curmax = alphabet.index(counts[i])
    for j in range(len(alphabet)):
        key[alphabet[(curmax + j)%26]] = alphabet[(4 + j)%26]

    for j in cipher:
        if j in alphabet:
            plain += key[j]
        else:
            plain += j

    print("\nGuess "+ i +":\n" + plain)
    
