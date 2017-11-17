alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
revalpha = alphabet[::-1]

cipher = input("Cipher:\n")
plain = ''

for i in cipher:
    plain += revalpha[alphabet.index(i)]

print(plain)
