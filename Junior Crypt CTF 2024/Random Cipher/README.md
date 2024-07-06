# Random cipher

You have received an encryption procedure that uses random numbers and text encrypted with it.

Restore the original message and find the flag in it.

## From description

There are two files provided, code_terror.py and terror.txt.

Presumably, terror.txt contains the output of running code_terror.py on the flag.

## Understanding code_terror.py

```
from random import randint

def encrypt(text):
    key = randint(1, 2 * len(text))
    print (ord(text[0]), key)
    result = []

    for c in text:
        result.append(ord(c) + (ord(c) % key))
        key = key + 1

    return result
```

The ```encrypt()``` function generates an integer from 1 to 2 * len(text) inclusive, which is the key.
Then, for every character in the flag, it converts it to a number using ```ord()```, and appends the number that results from the operation of ```ord(c) + ord(c) % key```.
%, or modulo, returns the remainder of the first number divided by the second number. Hence, if ```ord(c) = 57``` and ```key = 9```, ```ord(c) % key = 57 % 9 = 1```.
This is because the closest multiple of 9 to 57 is 9 * 6 = 56, and the remainder would be 57 - 56 = 1. 

## Decrypting the ciphertext

```result.append(ord(c) + (ord(c) % key))```

Let's let ```ord(c)``` be x., and the result of ```ord(c) + (ord(c) % key)``` be r. 

Hence, we get the equation ```r = x + x % key```. Now to make x the subject, x = 
