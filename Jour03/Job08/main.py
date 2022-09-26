import re
import matplotlib.pyplot as plt

regex = "(([a-z]|[A-Z])+)"
data = {}

f = open("data.txt", "rt")
text = f.read()
result = re.findall(regex, text)
for i in range(0, len(result)):
    if data.setdefault(len(result[i][0])) == None:
        data[len(result[i][0])] = 1
    else:
        data[len(result[i][0])] += 1
for key in list(data.keys()):
    data[key] = (data[key] / len(result)) * 100

plt.bar(list(data.keys()), list(data.values()))
plt.title("Repartition des lettres")
plt.xlabel("Longueur des mots")
plt.ylabel("Pourcentage")
plt.show()
f.close()