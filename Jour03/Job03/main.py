import re

regex = "(([a-z]|[A-Z])+)"

size = ""
while size.isdigit() == False:
    size = input("Veuillez entrer une taille valide de mots recherché : ")
size = int(size)
count = 0

f = open("data.txt", "rt")
text = f.read()
result = re.findall(regex, text)
for i in range(0, len(result)):
    if len(result[i][0]) == size:
        count += 1
print("There is", count, "word(s) of size", size, "in the text")
f.close()