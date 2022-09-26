def fact(nombre):
    if nombre == 1 or nombre == 0:
        return(1)
    else:
        return nombre * fact(nombre - 1)

nombre = input("Entrez un nombre : ")
while nombre.isdigit() == False:
    nombre = input("Entrez un nombre valide : ")
nombre = int(nombre)
print(fact(nombre))