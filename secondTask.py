"""" Write a Python program that replaces all but the last five characters of a string with "*" and returns the
modified string

Original String: kdi39323swe
new string: ******23swe
"""

original_string = "kdi39323swe"
replacement_char = "*"
size = len(original_string)
new_string = original_string[:size - 5]

for char in new_string:
    new_string = new_string.replace(char, replacement_char)

print(new_string + original_string[-5::])
