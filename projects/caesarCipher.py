#! /usr/bin/env python3
# caesarCipher.py - shift +3 cipher encoder/decoder

import sys
import pyperclip

cipherText = {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'u',
    's': 'v',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c',
    ' ': ' ', # white space text to avoid errors
}


if len(sys.argv) < 2: # shows the feature of the program 
    print("Usage: caesarCipher.py - encodes/decodes text in shift +3 encryption")
    sys.exit()

functionCipher = sys.argv[1] # terminal argument if user wants to encode/decode a text 
text = pyperclip.paste() # pasted text to be decoded/encoded

# avoids decimal and special characters from the pasted text
if text.isdecimal():
    print('Text must only have letters not numerical characters, please try again')
    sys.exit()

# splits the text to be decode/encoded
processedText = list(text)


finalText = [] # change the processedText to be encoded/decoded
if functionCipher.startswith("encode"): # encodes the pasted text
    for text in processedText:
        for k, v in cipherText.items():
            if text == k:
                finalText.append(v)
    print("Encrypted text copied to clipboard")
elif functionCipher.startswith("decode"): # decodes the pasted text
    for text in processedText:
        for v, k in cipherText.items():
            if text == k:
                finalText.append(v)
    print("Decrypted text copied to clipboard")
else:
    print("Error: function argument does not exist")
    sys.exit()

text = ''.join(finalText) # joins the final result of the encoded/decoded text
pyperclip.copy(text)