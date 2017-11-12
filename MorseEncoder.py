# Name: First Last
# Date:
# Period:
# Lab: MorseEncoder.py
# Description: Students use string processing and a python dictionary to create a morse code encoder
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#

from MorseDictionary import morse_code

# Create a function called morse_encoder(msg: str) that takes a single string parameter and converts it into the
# corresponding morse code message.  Note that the dictionary keys are all capital letters
# Sample input        -->     Return Value
# morse_encoder("A")        -->     ".-"
# morse_encoder("PYTHON")   -->     ".--.-.---....----."
def morse_encoder(msg: str):
    # TODO: Write the code for morse_encoder().

    return msg


# Create a function called morse_decoder(msg: str) that takes a single string parameter (in morse code) and converts it into the
# corresponding string message.  The message can be returned in all caps.
# Sample input                          -->     Return Value
# morse_decoder(".-")                   -->     "A"
# morse_decoder(".--.-.---....----.")   -->     "PYTHON"
def morse_encoder(morse_msg: str):
    # TODO: Write the code for morse_decoder().

    return ""


def main():
    # TODO: Write at least 4 tests to verify that morse_encoder() works.
    print("Morse Encoder Testing")


    # TODO: Write at least 4 tests to verify that morse_decoder() works.
    print("Morse Decoder Testing")


main()