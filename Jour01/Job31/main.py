lowest = 0
result = ""

def check_Value(word, tmp):
    i = 0
    diff = 0
    global lowest

    for i in range(len(word)):
        x = ord(word[i])
        y = ord(tmp[i])
        diff = diff * 10 + abs(x - y)
    if (diff < lowest or lowest == 0) and diff != 0:
        if diff > 0:
            lowest = diff
        return True
    return False



def combine(start, word, end, tmp):
    global lowest
    global result
    if start == end:
        if check_Value(word, tmp):
            result = tmp.copy()
    for i in range(start, end):
        tmp[start], tmp[i] = tmp[i], tmp[start]
        combine(start + 1, word, end, tmp)
        tmp[i], tmp[start] = tmp[start], tmp[i]

check = True
word = ""

while check:
    word = input("Veuillez entrer un mot valide : ")
    i = 0
    check = False
    while i < len(word):
        if word[i] < 'a' or word[i] > 'z':
            check = True
        i += 1

word = list(word)
combine(0, word, len(word), word.copy())
print("".join(result))