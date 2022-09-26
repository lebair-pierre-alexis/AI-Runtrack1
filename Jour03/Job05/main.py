import re
import matplotlib.pyplot as plt

regex = "([a-z]|[A-Z])"
data = {}

for leter in range(ord('a'), ord('z') + 1):
    data[chr(leter)] = 0
f = open("data.txt", "rt")
text = f.read()
result = re.findall(regex, text)
for e in result:
    e = e.lower()
    data[e] += 1
plt.bar(list(data.keys()), list(data.values()))
plt.title("Repartition des lettres")
plt.xlabel("lettres")
plt.ylabel("Nombre")
plt.show()
f.close()