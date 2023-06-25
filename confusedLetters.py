#! /usr/bin/env python3
# confusedLetters.py
# turn "hello" into "HeLlO"

import pyperclip
text = pyperclip.paste()

letters = list(text)


for index, letter in enumerate(letters):
    if index % 2 == 0:
        letters[index] = letter.upper()
    else:
        letters[index] = letter.lower()

text = ''.join(letters)
    

pyperclip.copy(text)