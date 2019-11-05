# Name: First Last
# Date:
# Period:
# Lab: MorseCode.py
# Description: Students use string processing and a python dictionary to create a morse code encoder
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#

from MorseDictionary import morse_code

# Create a function called morse_encoder(str_msg) that takes a single string parameter and converts it into the
# corresponding morse code message.  Note that the dictionary keys are all capital letters
# Sample input        -->     Return Value
# morse_encoder("A")        -->     ".-"
# morse_encoder("PYTHON")   -->     ".--. -.-- - .... --- -."
def morse_encoder(str_msg):
    # TODO: Write the code for the morse_encoder function.

    return ""


# Create a function called morse_decoder(morse_msg) that takes a single string parameter (in morse code) and converts it into the
# corresponding string message.  The message can be returned in all caps.
# Sample input                          -->     Return Value
# morse_decoder(".-")                   -->     "A"
# morse_decoder(".--. -.-- - .... --- -.")   -->     "PYTHON"
def morse_decoder(morse_msg):
    # TODO: Challenge - Write the code for the morse_decoder function.

    return ""


def main():
    # TODO: Write at least 4 tests to verify that your morse_encoder function works.
    print("Morse Encoder Testing")
    print("The message 'SOS' expected result: '... --- ...'", "\n\tActual result: ", morse_encoder("SOS"))
    
    print("\n\n")
    print("Morse Decoder Testing")
    print("The message '... --- ...' expected result: 'SOS'", "\n\tActual result: ", morse_decoder("... --- ..."))

if __name__ == "__main__": main()
