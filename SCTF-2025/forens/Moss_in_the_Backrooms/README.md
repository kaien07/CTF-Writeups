# Moss in the Backrooms

## description

WªHªAªTª ªAªRªEª ªTªHªEªSªEª ªCªHªAªRªAªCªTªEªRªSª ªWªHªEªRªEª ªIªSª ªMªYª ªJªPªGª ªAªAªAªAªAªAªAªAªAªAªAªAªAªAªAªAªAªHª

author: `__ytj__`

files provided: `Moss_in_the_Backrooms.jpg`

```
> file Moss_in_the_Backrooms.jpg
Moss_in_the_Backrooms.jpg: data
```

## solve

```
> xxd Moss_in_the_Backrooms.jpg | head
00000000: 7fd8 ffe1 0a57 c5f8 69e6 8000 4949 aa80  .....W..i...II..
00000010: 0880 8080 0a80 0e01 0280 a000 0080 8600  ................
00000020: 0080 8f81 8200 8580 0080 a600 0080 1001  ................
00000030: 0200 8e80 0000 2c00 0080 9201 8380 8100  ......,.........
00000040: 0000 8180 0080 9a81 0580 0180 8080 bc80  ................
00000050: 0000 9b81 0500 0180 0000 c480 0000 2801  ..............(.
00000060: 0300 8180 0000 0200 0080 b201 8200 9480  ................
00000070: 0080 4c80 8080 9382 0300 8180 0080 8200  ..L.............
00000080: 0000 e987 0480 0100 0080 e000 0000 e482  ................
00000090: 0080 a020 a020 a0a0 20a0 a0a0 a0a0 20a0  ... . .. ..... .
```

using a [file header lookup website](https://filesig.search.org/), i found that the correct `.jpg` header is `ff d8`. 

changing that gives me a wonderful picture of the backrooms, but unfortunately no flag.

looking closer at the challenge description, combined with the mangled bytes, there's a case to be made for the flag being hidden in the bytes.

reverting back to the original file, my first thought was msb (most significant byte).

taking the first eight bytes `7fd8 ffe1 0a57 c5f8` and taking msb of each nets us this binary value `01110011`.

converting it from binary in cyberchef returns us the character `s` which is the first letter of the flag format.

```
with open('Moss_in_the_Backrooms.jpg', 'rb') as f:
    a = f.read()

a = [i >> 7 for i in a]
p = []
for i in range(0, len(a), 8):
    s = [str(balls) for balls in a[i:i+8]]
    p.append(''.join(s))
# print(p)
print(''.join(p[:50]))
```

flag: `sctf{d0n7_100k_64ck}`

## afterthoughts

lowk kinda guessy but a solve is a solve and also technically the chall desc hinted at it
