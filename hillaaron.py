import numpy

def keyExit():
    input("Key Invalid")
    raise(SystemExit)

# a is the number you want the inverse for
# m is the modulus
# from https://numericalrecipes.wordpress.com/tag/modular-multiplicative-inverse/
def mod_inverse(a,m) :
    """
    Computes the modular multiplicative inverse of a modulo m,
    using brute force
    """
    a %= m
    for x in range(1,m) :
        if a*x%m == 1 :
            return x
    keyExit()

def invert(key):
    if len(key) == 2:
        n = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    elif len(key) == 3:
        n = key[0][0]*(key[1][1]*key[2][2] - key[1][2]*key[2][1]) - key[1][0]*(key[0][1]*key[2][2] - key[2][1]*key[0][2]) + key[2][0]*(key[0][1]*key[1][2] - key[1][1]*key[0][2])
    else:
        keyExit()
    determinant = mod_inverse(n%26,26)
    inverse = (determinant*numpy.asmatrix(key)).tolist()
    newinverse = []
    for x in inverse:
        minilist = []
        for y in x:
            minilist.append(int(y%26))
        newinverse.append(minilist)
    return newinverse
        
def hilldecrypt(ciphertext,key):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    period = len(key)

    inverse = numpy.asmatrix(invert(key))
    
    vectors = []
    minilist = []
    x = 1
    for letter in ciphertext:
        minilist.append(alphabet.index(letter.upper()))
        if x % period == 0:
            vectors.append(minilist)
            minilist = []
        x+=1

    nonsense = 0
    
    if len(minilist) != 0:
        while len(minilist) != period:
            minilist.append(-1)
            nonsense += 1
        vectors.append(minilist)

    matrixvector = []
    for x in range(0,period):
        minilist = []
        for vector in vectors:
            minilist.append(vector[x])
        matrixvector.append(minilist)

    matrix = numpy.asmatrix(matrixvector)
    
    result = (inverse * matrix).tolist()

    resultordered = []
    for x in range(0,len(result[0])):
        for y in range(0,period):
            resultordered.append(result[y][x]%26)

    finaltext = ""
    for x in range(0,len(resultordered)-nonsense):
        finaltext += alphabet[resultordered[x]]

    return finaltext
    
'''ciphertext = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
key = [[1,2,3],
       [1,2,3],
       [1,2,3]]
print(hilldecrypt(ciphertext,key))

key = [[1,2],
       [3,4]]
print(hilldecrypt(ciphertext,key))
'''
