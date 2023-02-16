original_string = "kdi39323swe"
replacement_char = "*"
size = len(original_string)
new_string = original_string[:size - 5]

for char in new_string:
    new_string = new_string.replace(char, replacement_char)

print(new_string + original_string[-5::])
