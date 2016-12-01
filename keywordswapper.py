alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
finished = ""
keyword = input("What is the keyword you would like to change?\n--> ")

for char in keyword:
    finished = finished + alphabet[(26 - alphabet.index(char))%26]

print(finished)
