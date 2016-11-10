ciphertext = input('Please enter the ciphertext.\n--> ')
split = int(input('Please enter how many characters you want to split it by. '))

def boxcode(c, n):
    cipher_split = [c[i:i+n] for i in range(0, len(c), n)]

    for block in cipher_split:
        print(block)

boxcode(ciphertext, split)

again = input('Do you want to try a different number of characters? (y/n) ')
if again == 'y':
    split = int(input('Please enter how many characters you want to split it by. '))
    boxcode(ciphertext, split)
