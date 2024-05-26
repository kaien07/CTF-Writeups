# XORry

Oops. I accidentally put my flag into this program and it spit out some garbage. Please get my flag back!

created by jp_var03

## From the decription of the challenge

The two files given are encrypt.py, the python file used to encrypt the plaintext, and encrypted.txt, the ciphertext.

As hinted by the name of the challenge, this challenge uses XOR.

## What is XOR?
XOR is a boolean logic operation, usually represented by the symbol ^.

1 ^ 0 = 1

1 ^ 1 = 0 ^ 0 = 0

As you can see, if the two numbers are different (i.e. 0 and 1), the result of their XOR will be 1, or True. Conversely, if the two numbers are the same, the result of their XOR will be 0, or False.

You can XOR two numbers by converting them to binary and looking at each individual digit in the binary string.

10 ^ 9 = 1010 ^ 1001 = 0011 = 3

## Understanding encrypt.py

```
import random

def shift_text_file(input_file, output_file):
    # Read content from the input file
    with open(input_file, 'r') as file:
        text_content = file.read()
    # Generate a random number from 0 to 50 for shifting
        num = random.randint(0, 50)
        print(num)
    # Shift the content by adding spaces
        new_text_content = ''.join([chr(ord(i) ^ num) for i in text_content])

    # Write the encrypted to the output file
    with open(output_file, 'w') as file:
        file.write(new_text_content)



input_text_file = 'flag.txt'
output_shifted_text_file = 'encrypted.txt'
shift_text_file(input_text_file, output_shifted_text_file)

```

How this program encrypts the plaintext is that it uses the random library, specifically the random.randint(0, 50) function. It generates a random integer num from 0 to 50, including both endpoints. 

```num = random.randint(0, 50)```

Then, using this integer, for every letter in the plaintext, it converts the letter into its Unicode equivalent using ord(), and does a XOR operation with num, before using chr() to convert the result of the XOR operation to obtain the character from its Unicode value. Finally, it concatenates all the individual encrypted characters, using ''.join().

```new_text_content = ''.join([chr(ord(i) ^ num) for i in text_content])```

## Decrypting the ciphertext

The ciphertext can be obtained through the provided file encrypted.txt. Since there is no way for us to know what the random number generated were, we will just have to try every number from 0 to 50, by using the range(51) function (range does not include the endpoint, but includes the start point, hence this generates all the numbers from 0 to 50). 

We can also reverse the XOR function.

a ^ b = c

c ^ b = a

As proof,

1010 ^ 0011 = 1001

1001 ^ 0011 = 1010

Hence, if we XOR the Unicode equivalent of each character in the ciphertext by the correct integer that was generated, and join them together, we will get the flag!

```
with open("encrypted.txt", 'r') as f:
    data = f.read()
    for num in range(51):
        decrypt = ''.join([chr(ord(char) ^ num) for char in data])
        print(decrypt)
        print("\n")
```

This program opens encrypt.txt, and reads the file as a string. It does a XOR operation for every character of the flag with num, and prints it out. It will print out 50 outputs, as there are 50 possible nums that the original plaintext could have been decrypted with.

To find the flag, all we need to do is to read through the output in the terminal and find the right flag.

Flag: btctf{X0Rry_fOr_mAkIN9_TH1s_7O0_ez}
