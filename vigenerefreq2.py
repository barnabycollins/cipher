alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
splits = []
plain = ''
vigkey = ''

cipher = input("Cipher:\n").upper()
keylen = int(input("What is the keyword length\n--> "))

for i in range(keylen):
    splits.append('')
    
for i in range(len(cipher)):
    splits[i%keylen] += cipher[i]

for i in range(keylen):
    key = {}
    counts = {}
    for j in alphabet:
        counts[j] = splits[i].count(j)

    counts = sorted(counts, key=counts.get, reverse=True)
    plain = ''
    curmax = alphabet.index(counts[0])
    for k in range(len(alphabet)):
        key[alphabet[(curmax + k)%26]] = alphabet[(4 + k)%26]

    for k in splits[i]:
        if k in alphabet:
            plain += key[k]
        else:
            plain += k
    vigkey += list(key.keys())[list(key.values()).index("A")]

for i in range(len(cipher)):
    plain += splits[i%keylen][i//keylen]
