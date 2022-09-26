def up_Grades(notes):
    i = 0
    while i != len(notes):
        if notes[i] % 5 >= 3 and notes[i] % 5 != 0:
            notes[i] += 5 - notes[i] % 5
        i += 1
    return notes

notes = [10, 85, 27, 34, 28, 98, 100, 99, 3, 7, 9, 69, 91, 22, 36]
print("Anciennes notes :", notes)
print("Notes arrondies :", up_Grades(notes))