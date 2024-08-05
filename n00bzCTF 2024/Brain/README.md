# Brain

Help! A hacker said that this "language" has a flag but I can't find it! 

Author: NoobMaster

## From description

There is one file given, bf.txt.

## Understanding bf.txt

bf.txt contains a bunch of symbols, all from our favourite esoteric language, brainf*ck! For more information on the different symbols, you can go [here](./../../BCACTF%202024/My%20Brain%20Hurts/README.md).

Let's take a look at a part of the script to see how it forms each character of the flag.

```>+++++++++++[<++++++++++>-]<[-]```

The script uses two storage "cells" as I will be calling them, which each stores one number.

`>` moves the pointer from cell 1 to cell 2

`+++++++++++` adds 11 to cell 2, leaving it at a value of 11.

`[<++++++++++>-]` signifies a loop. While the cell which the pointer is originally pointing to (cell 2) is more than zero, it will:
* `<` Move the pointer back to cell 1
* `++++++++++` Add 10 to cell 1
* `>` Move the pointer back to cell 2
* `-` Minus 1 from cell 2

At the moment, the values of cell 1 is 110 and the final value of cell 2 is 0.

`<[-]` The pointer moves back to cell 1, and runs a loop where it decreases the value in cell 1 by 1 until the value in cell 1 is 0. This is to reset the values of cell 1 and cell 2 for the next character.

The value which we are the most interested in is the one in cell 1 before it is resetted. You may notice that it is actually the product number of '+' in `>+++++++++++` and the number of '+' in `[<++++++++++>-]`, or in this case, 11 * 10 = 110.

The corresponding character for the ASCII code 110 is `n`, which fits in with the flag format of `n00bz{}`.

Doing the same checking for the next two parts of the code, `>++++++++[<++++++>-]<[-]` and `>++++++++[<++++++>-]<[-]`, gives us both 48, which incidentally translate to `0`, showing that we are on the right track, as so far we have `n00`, the first three letters of the flag.

Now how can we automate this?

## Writing solve.py

```
with open("bf.txt", "r") as f:
    bf = f.read()
bflst = bf.split("<[-]>")
bflst2 = []
for elem in bflst:
    bflst2.append(elem.split("["))
for elem in bflst2:
    print(chr(elem[0].count("+") * elem[1].count("+")), end="")
```

The way I approached it was first by separating the the script into the parts that make up each character. We can do this by spliting it with the separator `<[-]>`, as this is only meant for the resetting of the two cells.

Then, I split it again with `[`, the start of the loop.

Hence, using the first part `>+++++++++++[<++++++++++>-]` as an example, I had now split it into two parts, `>+++++++++++` and `<++++++++++>-]`.

Now, following the observations above, all we have to do is multiply the number of `+` in the first part to the number of `+` in the second part to get the ASCII value of the character.

Finally, I used `chr()` to convert the ASCII values to the characters of the flag.

## Alternate method
Another way is, in every part of the script, using an example of `>+++++++++++[<++++++++++>-]<[-]`, we can add a `.` before the loop to reset the cells, such that the part is modified to be `>+++++++++++[<++++++++++>-]<.[-]`.

`.` means to output the value in the cell that the pointer is pointing to. 

This gives you the script:

```
>+++++++++++[<++++++++++>-]<.[-]>++++++++[<++++++>-]<.[-]>++++++++[<++++++>-]<.[-]>++++++++++++++[<+++++++>-]<.[-]>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++>-]<.[-]>+++++++++++++++++++++++++++++++++++++++++[<+++>-]<.[-]>+++++++[<+++++++>-]<.[-]>+++++++++++++++++++[<+++++>-]<.[-]>+++++++++++[<+++++++++>-]<.[-]>+++++++++++++[<++++>-]<.[-]>+++++++++++[<++++++++++>-]<.[-]>+++++++++++++++++++[<+++++>-]<.[-]>+++++++++++[<+++++++++>-]<.[-]>++++++++[<++++++>-]<.[-]>++++++++++[<++++++++++>-]<.[-]>+++++++++++++++++[<+++>-]<.[-]>+++++++++++++++++++[<+++++>-]<.[-]>+++++++[<+++++++>-]<.[-]>+++++++++++[<++++++++++>-]<.[-]>+++++++++++++++++++[<+++++>-]<.[-]>++++++++++++++[<+++++++>-]<.[-]>+++++++++++++++++++[<++++++>-]<.[-]>+++++++++++++[<++++>-]<.[-]>+++++++[<+++++++>-]<.[-]>+++++++++++[<++++++++++>-]<.[-]>+++++++++++++++++[<++++++>-]<.[-]>+++++++[<++++++>-]<.[-]>+++++++++++[<+++++++++>-]<.[-]>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+>-]<.[-]>+++++++++++[<+++>-]<.[-]>+++++++++++++++++++++++++[<+++++>-]<.[-]
```

We can then run it using https://www.dcode.fr/brainfuck-language.

Flag: n00bz{1_c4n_c0d3_1n_br41nf*ck!}
