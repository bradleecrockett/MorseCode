# MorseCode
Morse code encoder and decoder using python dictionaries.

## Intro to Dictionaries
Watch the video https://youtu.be/wa1XcMSBWdA and follow along on `dictionary_notes.py`. You will use a dictionary in your morse code encoder and decoder program.

You should be able to anser the following questions:
1) What is a dictionary?
2) How do you declare a dictionary?
3) How do you access elements of a dictionary?
4) Do dictionaries have an order?
5) What is a key value pair?
6) Name 3 useful methods that are associated with dictionaries.


## Morse Encoder Function
Create a function called morse_encoder(str_msg) that takes a single string parameter and converts it into the
corresponding morse code message.  Note that the dictionary keys are all capital letters

| Sample input | Return Value |
| --- | --- |
| morse_encoder("A") | ".-" |
| morse_encoder("PYTHON")   |     ".--. -.-- - .... --- -." |

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
    print("The message 'S O S' expected result: '... --- ...'", "\n\tActual result: ", morse_encoder("S O S"))


if __name__ == "__main__": main()
```

## Morse Decoder
Challenge a function called morse_decoder(morse_msg) that takes a single string parameter (in morse code) and converts it into the
corresponding string message.  The message can be returned in all caps. Note that you may need to make some changes in order to 
make this work...

| Sample input      | Return Value |
| --- | --- |
| morse_decoder(".-")                  |     "A" |
| morse_decoder(".--. -.-- - .... --- -.")  |     "P Y T H O N" |

```python
def morse_decoder(morse_msg):
    # TODO: Challenge - Write the code for the morse_decoder function.

    return ""
```

## Morse Decoder Tests

Add at least 4 tests to the main() method to test the decoder function that you created.

```python
    
    print("Morse Decoder Testing")
    print("The message '... --- ...' expected result: 'S O S'", "\n\tActual result: ", morse_decoder("... --- ..."))
    
```

