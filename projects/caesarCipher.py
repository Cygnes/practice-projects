# caesarCipher.py - shift +3 cipher encoder/decoder
import sys

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

def encodeText(cipherText, processedText):
    finalText = []
    for text in processedText:
        for k, v in cipherText.items():
            if text == k:
                finalText.append(v)

    return ''.join(finalText)

def decodeText(cipherText, processedText):
    finalText = []
    for text in processedText:
        for v, k in cipherText.items():
            if text == k:
                finalText.append(v)
    
    return ''.join(finalText)

def main(): 
    while True: 
        text = input("Enter text here or press Q to quit: ")
        # Quits the encoder/decoder 
        if text.startswith("Q"):
            sys.exit()
        # avoids decimal and special characters from the pasted text
        if text.isdecimal():
            print('Text must only have letters not numerical characters, please try again')
            sys.exit()

        user = input("Encode/Decode: (E | D) ")

        # splits the text to be decode/encoded
        processedText = list(text.lower())

        if user == "E": # encodes the pasted text
            text = encodeText(cipherText, processedText)
        elif user == "D": # decodes the pasted text
            text = decodeText(cipherText, processedText) 
        else:
            print("Error: command does not exist")
            sys.exit()

        print(f"Final Result: {text}")
        
if __name__ == "__main__":
    main()