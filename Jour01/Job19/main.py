width = int(input("Veuillez choisir la largeur du rectangle : "))
height = int(input("Veuillez choisir la hauteur du rectangle : "))
line = 0
rectangle = ""

while line != height:
    col = 0
    while col != width:
        if col == 0 or col == width - 1:
            rectangle += "|"
        else:
            rectangle += "-"
        col += 1
    rectangle += "\n"
    line += 1

print(rectangle)