numbers = []
i = 0

while i != 5:
    print("Saisir le nombre", i + 1)
    numbers.append(int(input()))
    i += 1
numbers.sort()
print(numbers)
