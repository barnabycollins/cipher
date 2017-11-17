cipher = input("cipher:\n")
current = ''
combos = {}

for i in cipher:
    if(i == " "):
        if(current in combos):
            combos[current] += 1
        else:
            combos[current] = 1

        current = ''

    else:
        current += i

combos[current] = 1

for i in sorted(combos, key=combos.get, reverse=True):
    print(i + ": " + str(combos[i]))
