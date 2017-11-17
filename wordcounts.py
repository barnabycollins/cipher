alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
current = ""
cipher = input("Cipher:\n").upper()
text = ''
counts = {}
for i in cipher:
    if i in alphabet or i == " ":
        text += i

lengths = []

for i in cipher:
    if i == " ":
        lengths.append(current)
        current = ''
    else:
        current += i

for i in lengths:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

sorteddict = sorted(counts, key=counts.get, reverse=False)
for i in sorteddict:
    print(i + ": " + str(counts[i]))
