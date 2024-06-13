# My Brain Hurts

My friend sent me a weird string and a "program" they wrote, although it doesn't seem anything interpretable to me. Can you help me find out what they put through their program?

By Kai Lindemer

## From description

The two files given are script.txt, the program used to encrypt the text, and string.txt, the output of the text.

## Understanding script.txt

Opening script.txt made me go o_O.

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


