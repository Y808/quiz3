"""
Write a program to make a list of words from a given sentence by splitting them.
Rules:
1- "n/a" should be replaced by "A",
2- Words should be created by splitting from the spaces.

given = "I am n/a QA n/automation Engineer"
output = ['I', 'am', 'a', 'QA', 'Automation', 'Engineer']
"""

given_string = "I am n/a QA n/automation Engineer"
new_string = given_string.replace("n/a", "A")
print(new_string.split(" "))

