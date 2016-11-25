#By AARON GILCHRIST ( https://agilchrist0.github.io )
def createKey(keyword):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    ciphertext_alphabet = []

    for letter in keyword:
        if letter.upper() not in ciphertext_alphabet:
            ciphertext_alphabet.append(letter.upper())

    last_letter = ciphertext_alphabet[-1]
    letter_number = alphabet.index(last_letter)

    for burger in range(letter_number+1, len(alphabet)):
        cake = alphabet[burger]
        if cake not in ciphertext_alphabet:
            ciphertext_alphabet.append(cake)

    for chip in range(0, len(alphabet)):
        rice = alphabet[chip]
        if rice not in ciphertext_alphabet:
            ciphertext_alphabet.append(rice)

    for x in range(0,26):
        alphabet[x] = alphabet[x].lower()

    key = dict(zip(ciphertext_alphabet,alphabet))

    return key

def encode(code,msg):
    for k,v in code.items():
        msg = msg.replace(k, v)
    return msg

def crackKeyword():
    keyword = input('Please enter a suitable keyword:\n--> ')
    key = createKey(keyword)
    ciphertext = input('\nPlease enter your ciphertext:\n--> ').upper()
    result = encode(key,ciphertext)
    print('This is the result:\n{}'.format(result))

crackKeyword()
