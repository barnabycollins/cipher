alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

plain = ""

cipher = input("cipher\n").upper()
for letter in cipher:
    if letter in alphabet:
        plain += letter

print("\n" + plain)
