# Exercise 131: Morse Code
#
# Morse code is an encoding scheme that uses dashes and dots to represent numbers and letters.
# In this exercise, you will write a program that uses a dictionary to store the mapping from letters and numbers to Morse code.
# Use a period to represent a dot, and a hyphen to represent a dash. The mapping from letters and numbers to dashes
# and dots is shown in Table 6.1.
# Your program should read a message from the user. Then it should translate each
# letter and number in the message to Morse code, leaving a space between each sequence of dashes and dots.
# Your program should ignore any characters that are not letters or numbers. The Morse code for Hello, World! is shown below:
# .... . .-.. .-.. --- .-- --- .-. .-.. -..

dict_morse_code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

user_input = 'Hello, World!'.upper()

for item in user_input:
    for k,v in dict_morse_code.items():
        if k == item:
            print(v, end=" ")
print()
