cipher = input("Cipher:\n")
number = int(input("\nNumber fing\n--> "))
finished = ""

for j in range(number):
    for i in range(int(len(cipher)/number)):
        finished = finished + cipher[number*i + j]

print(finished)
