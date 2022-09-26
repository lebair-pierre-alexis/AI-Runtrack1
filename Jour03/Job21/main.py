from cProfile import label
import re
import matplotlib.pyplot as plt
from collections import OrderedDict

regex = "([a-z]|[A-Z])"
data = {}

f = open("data.txt", "rt")
text = f.read()
result = re.findall(regex, text)
for i in range(0, len(result)):
    result[i] = result[i].lower()
    if i != len(result) - 1:
        if data.setdefault(result[i]) == None:
            data[result[i]] = {}
        next = result[i + 1].lower()
        if data[result[i]].setdefault(next) == None:
            data[result[i]][next] = 1
        else:
            data[result[i]][next] += 1
for dic in data:
    data[dic] = OrderedDict(sorted(data[dic].items()))
data = OrderedDict(sorted(data.items()))
for dic in data:
    total = 0
    for key in data[dic]:
        total += data[dic][key]
    for key in data[dic]:
        data[dic][key] = (data[dic][key] / total) * 100
for dic in data:
    plt.plot(list(data[dic].keys()), list(data[dic].values()), label = "Lettre : " + dic)
plt.title("Nombre d'occurences des lettres après une lettre définie")
plt.legend()
plt.xlabel("Lettres suivantes")
plt.ylabel("Nombre d'occurences")
plt.show()
f.close()