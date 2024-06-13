# My Brain Hurts

My friend sent me a weird string and a "program" they wrote, although it doesn't seem anything interpretable to me. Can you help me find out what they put through their program?

By Kai Lindemer

## From description

The two files given are script.txt, the program used to encrypt the text, and string.txt, the output of the text.

## Understanding script.txt

When I first opened script.txt, my face looked like this: o_O.

```
,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,>,<----<++++++<---------<++<-<+++++<-------<+++++++++<-------<----<---<++++<--<+++<+++++++<+++<+<++<---------------<+++++<-------<---<----.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.
```

This is obviously not a conventionally used language, and so our first step would be finding out what this language is.

Searching for a code detector on google yields https://creativetechguy.com/utilities/codedetector. Going onto this website and running the code through it gives us Javascript. But wait a second...that isn't Javascript! Unchecking the "Common Languages Only" checkmark gives us a different result: brainf*ck.

Googling the language gives us its wikipedia page: https://en.wikipedia.org/wiki/Brainfuck. In there, it tells you what every symbol (there's only 6!) in the language does.

| Symbol | Description |
| ------ | ----------- |
| > | Increment the data pointer by one (to point to the next cell to the right) |
| < | Decrement the data pointer by one (to point to the next cell to the left) |
| + | Increment the byte at the data pointer by one |
| - | Decrement the byte at the data pointer by one |
| . | Output the byte at the data pointer |
| , | Accept one byte of input, storing its value in the byte at the data pointer |
| [ | If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command |
| ] | If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command |

So with these explanations for the various symbols, we can go ahead and get a good understanding of the script.

```
,> // c1 takes input (1 byte)
,> // c2 takes input
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,>
,> // c23 takes input
, // c24 takes input
<---- // c23 = c23-4
<++++++ // c22 = c22+6
<--------- // c21 = c21-9
<++ // c20 = c20+2
<- // c19 = c19-1
<+++++ // c18 = c18+5
<------- // c17 -7
<+++++++++ // c16 +9
<------- // c15 -7
<---- // c14 -4
<--- // c13 -3
<++++ // c12 +4
<-- // c11 -2
<+++ // c10 +3
<+++++++ // c9 +7
<+++ // c8 +3
<+ // c7 +1
<++ // c6 +2
<--------------- // c5 -15
<+++++ // c4 +5
<------- // c3 -7
<--- // c2 -3
<---- // c1 -4
.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>. // outputting all the characters of the flag
```

c in this explanation is referring to a "cell", a byte of stored data. Since the script takes in 24 bytes of data, the flag is 24 characters long. In the line where the 23rd character is being modified, ```<---- //c23 = c23-4```, the minus sign ```-``` is referring to a decrease in its ascii value, hence if the character 'f' was stored in c23, the result of the modification would be the ASCII code of 'f' - 4, which is 66 - 4 = 62, which when converted from ASCII code to its corresponding value, produces the letter 'b'.

## Obtaining the flag

Since we have to reverse the function (this is a reverse engineering challenge after all), all we have to do is take each individual character of the ciphertext, and reverse the specific modification that was made with the script.
