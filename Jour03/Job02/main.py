import re

regex = "([a-z]|[A-Z])+"

f = open("data.txt", "rt")
text = f.read()
result = re.findall(regex, text)
print("There is", len(result), "word(s) in the text")
f.close()