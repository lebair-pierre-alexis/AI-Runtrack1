from collections import OrderedDict
import re
import matplotlib.pyplot as plt

regex = "(([a-z]|[A-Z])+)"
data = {}

f = open("data.txt", "rt")
text = f.read()
result = re.findall(regex, text)
for i in range(len(result)):
    letter = result[i][0][0].lower()
    if data.setdefault(letter) == None:
        data[letter] = 1
    else:
        data[letter] += 1

data = OrderedDict(sorted(data.items()))

plt.bar(list(data.keys()), list(data.values()))
plt.title("Nombre d'occurence de chaque lettre en début de mot")
plt.xlabel("Lettres")
plt.ylabel("Nombre d'occurence")
plt.show()
f.close()