# BARNABY'S BOX CIPHER SOLVER V1.0 https://github.com/barnstorm3r
# 10/11/2016 DEVELOPED IN PYTHON 3.5.2
cipher = input("Cipher:\n")
boxnum = int(input("How wide are the boxes?\n--> "))
boxes = []
currentstr = ""
move = []
rearranged = []
condensed1 = []
condensed2 = ""

if len(cipher) % boxnum != 0:
    procede = input('Hmm. You are going to have characters left over. Do you want to procede? (y/n) ')
    if procede == 'y' or procede == 'Y':
        boxes = [cipher[i:i+boxnum] for i in range(0, len(cipher), boxnum)]
    else:
        print('Bye.')
        import sys
        sys.exit()
else:
    boxes = [cipher[i:i+boxnum] for i in range(0, len(cipher), boxnum)]

print(boxes)

for i in range(boxnum):
    move.append(int(input("Where should character " + str(i+1) + " go?\n--> ")) - 1)

for i in range(len(boxes)):
    rearranged.append([])
    for j in range(boxnum):
        rearranged[i].append("")

    for j in range(boxnum):
        rearranged[i][move[j]] = boxes[i][j]

for i in range(len(boxes)):
    condensed1.append("".join(rearranged[i]))

condensed2 = "".join(condensed1)

print("Plaintext: " + condensed2)
