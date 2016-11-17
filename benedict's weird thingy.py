cipher = input("Cipher:\n")
split = int(input("\nHow big would you like the splits to be?\n--> "))

stuff = []
# THIS IS A PRETTY CIPHER AND MR EVANS CAN'T SAY OTHERWISE, EVERYONE IS PRETTY IN THEIR OWN WAY, EVEN ME (I THINK)

for i in range(split):
    stuff.append("")

i = 0
for letter in cipher:
    stuff[i%3] = stuff[i%3] + letter
    i+=1

for i in stuff:
    print(i)
