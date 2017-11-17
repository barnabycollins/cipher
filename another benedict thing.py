cipher = input("Cipher:\n")
number = int(input("\nNumber fing\n--> "))
splits = []

for i in range(number):
    splits.append("")

for i in range(len(cipher)):
    splits[i%number] += cipher[i]
for i in splits:
    print(i)
