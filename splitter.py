cipher = input("Cipher:\n")
current = ''
splits = []
for i in range(len(cipher)):
    current += cipher[i]
    if(i%15) == 14:
        splits.append(current)
        current = ''

for i in splits:
    print(i)
