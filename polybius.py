import itertools

psquare = [['A','F','L','Q','V'],
           ['B','G','M','R','W'],
           ['C','H','N','S','X'],
           ['D','I','O','T','Y'],
           ['E','K','P','U','Z']]

cipher = input("cipher:\n")

perms = list(itertools.permutations(["D", "X", "C", "L", "M"]))
polydec = {}
plains = []

for i in range(len(perms)):
    nums = ''
    for j in range(5):
        polydec[perms[i][j]] = j
    for j in cipher:
        if j in polydec:
            nums += str(polydec[j])
    plains.append('')
    for j in range(int(len(nums)/2)):
        plains[i] += psquare[int(nums[j*2+1])][int(nums[j*2])]

    print(str(i) + ": " + plains[i][:20])

print(plains[int(input("Correct one?\n--> "))])
