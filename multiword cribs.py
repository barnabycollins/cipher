alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
current = ""
cipher = input("Cipher:\n").upper()
text = ''
for i in cipher:
    if i in alphabet or i == " ":
        text += i

lengths = []

for i in cipher:
    if i == " ":
        lengths.append(len(current))
        current = ''
    else:
        current += i

print("Word lengths list generated.")

# check for agricola
for i in range(len(lengths) - 2):
    if lengths[i] == 6 and lengths[i+1] == 6 and lengths[i+2] == 8:
        print("potential match for Agricola found at word " + str(i))

# check for ixth legion(s)
for i in range(len(lengths) - 1):
    if lengths[i] == 4 and (lengths[i+1] == 6 or lengths[i+1] == 7):
        print("potential match for IXth Legion(s) found at word " + str(i))

# check for boudicca
for i in range(len(lengths) - 1):
    if lengths[i] == 5 and lengths[i+1] == 8:
        print("potential match for Queen Boudicca found at word " + str(i))

# check for nero
for i in range(len(lengths) - 4):
    if lengths[i] == 8 and lengths[i+1] == 6 and lengths[i+2] == 8 and lengths[i+3] == 10 and lengths[i+4] == 4:
        print("potential match for Nero found at word " + str(i))

# check for firmus
for i in range(len(lengths) - 5):
    if lengths[i] == 9 and lengths[i+1] == 7 and lengths[i+2] == 6 and lengths[i+3] == 11 and lengths[i+4] == 7 and lengths[i+5] == 6:
        print("potential match for Firmus found at word " + str(i))

# check for gallicanus
for i in range(len(lengths) - 2):
    if lengths[i] == 5 and lengths[i+1] == 9 and lengths[i+2] == 10:
        print("potential match for Firmus found at word " + str(i))
        
