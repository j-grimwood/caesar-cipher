#! /usr/bin/python
'''
File name: caesarcipher.py
Author: Jess Grimwood
Date: 06/27/18
Python Version: 3.6
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift(offset):
    
    message = input("Input Message You Would Like Encrypted:\n")
    new_message = ''

    for letter in message:

        letter = letter.lower() #doesn't handle upper-case yet
    
        if letter.isalpha():
            shift_pos = alphabet.index(letter) + offset
            new_pos = alphabet[shift_pos]
            new_message += new_pos
        
        elif ' ' or '/t' or '/n' in letter: #pass these guys straight through
            new_message += letter
        
        elif letter.isnumeric():
            new_message += letter
        
        else:
            print("An error took place in recording the message. Check input.\n")

    print(new_message)


shift(-1)


