key = {}
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
current = ''

i = 0
for letter in alphabet:
    current = input('Please enter the plaintext of cipher ' + alphabet[i] + '.\n--> ')
    if current == '' or len(current) >1:
        if(input("Error: Invalid value entered.\nIs this intentional? (y/n)\n--> ") == "n"):
            current = input('Please enter the plaintext of cipher ' + alphabet[i] + '.\n--> ')
            key[letter] = current
    
    else:
        key[letter] = current
    
    i = i + 1

print(key)

cipher = input('Please paste the cipher:\n')
plain = ''

for character in cipher:
    if(character in key):
        plain = plain + key[character]

    else:
       plain = plain + character

print(plain)
