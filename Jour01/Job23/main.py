height = int(input("Veuillez choisir le nombre d'étages du triangle : "))
line = height
triangle = ""

while line != 0:
    fillers = line - 1
    while fillers:
        triangle += " "
        fillers -= 1
    triangle += "/"
    fillers = 1 + 2 * (height - line)
    while fillers:
        if line == 1:
            triangle += "_"
        else:
            triangle += " "
        fillers -= 1
    triangle += "\\"
    triangle += "\n"
    line -= 1

print(triangle)