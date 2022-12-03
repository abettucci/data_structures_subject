def most_common_letter():
    string = str(input('Ingresar frase: '))
    letters = set(string)
    if " " in letters:         # If you want to count spaces too, ignore this if-statement
        letters.remove(" ")
    max_count = 0
    freq_letter = []
    for letter in letters:
        count = 0
        for char in string:
            if char == letter:
                count += 1
        if count == max_count:
            max_count = count
            freq_letter.append(letter)
        if count > max_count:
            max_count = count
            freq_letter.clear()
            freq_letter.append(letter)
    return freq_letter, max_count

print(most_common_letter())