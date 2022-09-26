def up_Grades(notes):
    i = 0
    while i != len(notes):
        if notes[i] % 5 >= 3 and notes[i] % 5 != 0:
            notes[i] += 5 - notes[i] % 5
        i += 1
    return notes