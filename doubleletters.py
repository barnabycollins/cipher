cipher = input("cipher:\n")
finished = ""
doubles = ""
beforebeforebeforebeforelast = ""
beforebeforebeforelast = ""
beforebeforelast = ""
beforelast = ""
last = ""

for letter in cipher:
    if letter == beforebeforebeforebeforelast and beforebeforelast == beforebeforebeforelast:
        finished = finished + letter.lower()
        doubles = doubles + beforebeforebeforebeforelast + beforebeforebeforelast + beforebeforelast + beforelast + last + letter + " "
        print("Manish")
    else:
        finished = finished + letter

    beforebeforebeforebeforelast = beforebeforebeforelast
    beforebeforebeforelast = beforebeforelast
    beforebeforelast = beforelast
    beforelast = last
    last = letter

print(finished)
print(doubles)
