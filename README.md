# MorseCode
Morse code encoder and decoder using python dictionaries.

## Morse Encoder Function
Create a function called morse_encoder(str_msg) that takes a single string parameter and converts it into the
corresponding morse code message.  Note that the dictionary keys are all capital letters

| Sample input | Return Value |
| --- | --- |
| morse_encoder("A") | ".-" |
| morse_encoder("PYTHON")   |     ".--.-.---....----." |

```python
def morse_encoder(str_msg):
    # TODO: Write the code for morse_encoder().

    return ""
```

## Morse Encoder Tests
Write at least 4 more tests to verify that your morse encoder properly encodes messages. 
Each test should include an expected output and a call to your function to test it.
You may want to look up an online coverter tool to help you determine the proper encoding of a particular message.

```python
def main():
    # TODO: Write at least 4 tests to verify that your morse_encoder function works.
    print("Morse Encoder Testing")
    print("The message 'SOS' expected result: "...---...", "\n\tActual result: ", morse_encoder("SOS"))


if __name__ == "__main__": main()
```

## Morse Decoder
Challenge a function called morse_decoder(morse_msg) that takes a single string parameter (in morse code) and converts it into the
corresponding string message.  The message can be returned in all caps. Note that you may need to make some changes in order to 
make this work...

| Sample input      | Return Value |
| --- | --- |
| morse_decoder(".-")                  |     "A" |
| morse_decoder(".--.-.---....----.")  |     "PYTHON" |

```python
def morse_decoder(morse_msg):
    # TODO: Challenge - Write the code for the morse_decoder function.

    return ""
```

## Morse Decoder Tests

Add at least 4 tests to the main() method to test the decoder function that you created.

```python
    
    print("Morse Decoder Testing")
    print("The message '...---...' expected result: "SOS", "\n\tActual result: ", morse_encoder("...---..."))
    
```

