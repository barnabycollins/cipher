cipher = input("Cipher:\n")
letter = input("Letter:\n--> ")
letternums = []

for i in range(len(cipher)):
    if cipher[i] == letter:
        letternums.append(i)

print(letternums)
