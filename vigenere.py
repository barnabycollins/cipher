alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cipher = input("Cipher:\n")
keyword = input("\nKeyword in caps:\n-->")
keywordnums = []
finished = ""
menu = input("Which type of keyword are you using?\n1. Cipher to Plain\n2. Plain to Cipher\n--> ")

if menu == "1":
    for char in keyword:
        keywordnums.append(alphabet.index(char) + 1)
    
elif menu == "2":
    for char in keyword:
        keywordnums.append(25 - alphabet.index(char))

i = 0
for letter in cipher:
    finished = finished + alphabet[(alphabet.index(letter) + keywordnums[i])%26]
    i = i + 1
    if i == len(keyword):
        i = 0

print(finished)
