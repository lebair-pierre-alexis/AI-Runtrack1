import re

f = open("domains.xml", "rt")
i = 0
regex = "(\w+\.)+([a-z]+)"
for line in f:
    found = re.findall(regex, line)
    if (found):
        i += 1
print("Found", i, "matche(s)")
f.close()