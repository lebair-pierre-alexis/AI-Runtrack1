from collections import OrderedDict
import random
import re
import matplotlib.pyplot as plt

def createWord(o_size, size, letter, datas):
    my_list = []

    #This part will choose a letter based on the one
    #that was before
    for key in datas[letter]:
        for i in range(0, datas[letter][key]):
            my_list.append(key)
    if (size == 0):
        return random.choice(my_list)
    else:
        choice = random.choice(my_list)

        #Then when the random choice is made
        #we simply call back the function until
        #there si no more letter to pick
        if (o_size == size):
            return letter + createWord(o_size, size - 1, choice, datas)
        else:
            return choice + createWord(o_size, size - 1, choice, datas)

regex_letters = "([a-z]|[A-Z])"
regex_words = "(([a-z]|[A-Z])+)"
wordSizeData = {}
wordFirstData = {}
lettersData = {}
wordSize = []
wordFirst = []

f = open("data.txt", "rt")
text = f.read()
result_letters = re.findall(regex_letters, text)
result_words = re.findall(regex_words, text)

#Calculating the number of occurence for each size of word
for i in range(0, len(result_words)):
    if wordSizeData.setdefault(len(result_words[i][0])) == None:
        wordSizeData[len(result_words[i][0])] = 1
    else:
        wordSizeData[len(result_words[i][0])] += 1

#Calculating the number of occurence of each letter being
#the first letter of a word
for i in range(len(result_words)):
    letter = result_words[i][0][0].lower()
    if wordFirstData.setdefault(letter) == None:
        wordFirstData[letter] = 1
    else:
        wordFirstData[letter] += 1

#For a given letter, calculating the number of occurence of
#each letter being the next
for i in range(0, len(result_letters)):
    result_letters[i] = result_letters[i].lower()
    if i != len(result_letters) - 1:
        if lettersData.setdefault(result_letters[i]) == None:
            lettersData[result_letters[i]] = {}
        next = result_letters[i + 1].lower()
        if lettersData[result_letters[i]].setdefault(next) == None:
            lettersData[result_letters[i]][next] = 1
        else:
            lettersData[result_letters[i]][next] += 1

#Transforming the dictionnaries into 1 dimension lists
#Each list is made of the data (being a size or a letter)
#that has been appended n times
#(n being the number of occurence for this specific data)
for key in wordSizeData:
    for i in range(0, wordSizeData[key]):
        wordSize.append(str(key))
for key in wordFirstData:
    for i in range(0, wordFirstData[key]):
        wordFirst.append(key)

#Picking a random value from the differents list
#that have been weighted by the numbre of occurences
size = int(random.choice(wordSize))
first = random.choice(wordFirst)
print("Word of size", size, "and of first letter", first, ":", createWord(size - 1, size - 1, first, lettersData))
