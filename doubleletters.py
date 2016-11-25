cipher = input("cipher:\n")

last = []
beforebeforebeforebeforelast = ""
beforebeforebeforelast = ""
beforebeforelast = ""
beforelast = ""
last = ""
finished = ""
doubles = ""

for letter in cipher:
    if letter == beforebeforebeforebeforelast and beforebeforelast == beforebeforebeforelast:
        doubles = doubles + beforebeforebeforebeforelast + beforebeforebeforelast + beforebeforelast + beforelast + last + letter + " "
        print("Manish")


    beforebeforebeforebeforelast = beforebeforebeforelast
    beforebeforebeforelast = beforebeforelast
    beforebeforelast = beforelast
    beforelast = last
    last = letter

print(doubles)
