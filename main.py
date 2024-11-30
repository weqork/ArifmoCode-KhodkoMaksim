freq = {'а': 1, 'с': 1, 'х': 1, 'д': 1, 'ю': 1, 'р': 1, 'е': 1, 'в': 1, 'ч': 1, 'м': 2, 'к': 2, 'и': 2, 'о': 2, 'ь': 2, }
word = "ходькомаксимюрьевич"
total = 19
probability_of_symbols = {}
for current_symb in freq:
    probability_of_symbols[current_symb] = freq[current_symb] / total
current_left = 0
left_borders = {}
right_borders = {}
for current_symb in probability_of_symbols:
    left_borders[current_symb] = current_left
    right_borders[current_symb] = current_left + probability_of_symbols[current_symb]
    current_left += probability_of_symbols[current_symb]
print(left_borders)
print("______________")
print(right_borders)
left = 0.0
right = 1.0
for current_symb in word:
    section = right - left
    right = left + section * right_borders[current_symb]
    left = left + section * left_borders[current_symb]
lef = len(str(left)) - 2
binotvet = bin(int(left*(10 ** lef)))
print(binotvet [2:])
