alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cipher = input("Cipher:\n")
keyword = input("Keyword in caps:\n-->")
keywordnums = []
finished = ""

for char in keyword:
    keywordnums.append(alphabet.index(char) + 1)

i = 0
for letter in cipher:
    finished = finished + alphabet[(alphabet.index(letter) + keywordnums[i])%26]
    i = i + 1
    if i == len(keyword):
        i = 0

print(finished)
