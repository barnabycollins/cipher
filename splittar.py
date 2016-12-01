cipher = input("Cipher:\n")
wordlen = int(input("\nKeyword:\n--> "))
finished = []

for i in range(len(cipher) // wordlen):
    finished.append(cipher[i*wordlen:(i+1)*wordlen])

finished.append(cipher[len(cipher)-len(cipher)%wordlen:])

print(finished)
