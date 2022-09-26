def power(nombre, puissance):
    if puissance == 0:
        return(1)
    else:
        return nombre * power(nombre, puissance - 1)

nombre = input("Entrez un nombre : ")
puissance = input("Entrez un exposant : ")
while nombre.isdigit() == False:
    nombre = input("Entrez un exposant valide : ")
while puissance.isdigit() == False:
    puissance = input("Entrez un exposant valide : ")
nombre = int(nombre)
puissance = int(puissance)
print(power(nombre, puissance))