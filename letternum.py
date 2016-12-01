alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
menu = input("Do you have a:\n1. Letter\n2. Number\n--> ")
if menu == "1":
    letter = input("\nWhat is the letter?\n--> ")
    for i in letter:
        print("The letter " + i + " is number " + str(alphabet.index(i)))

elif menu == "2":
    number = int(input("\nWhat is the number?\n--> "))
    print("The letter at your number is " + alphabet[number])
