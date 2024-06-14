![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/ba1d645d-30d8-45da-802d-edb5ed28bed0)# Broken C Code

Help! I was trying to make a flag printer but my C code just prints random garbage and I can't figure out why! Can you help me? Here's the file:

By Jacob Korn

## From description

There is a file given, flagprinter, and it appears to be an executable. So let's boot up the VM and execute it!

## Understanding flagprinter

Running the executable with ```./flagprinter``` gives us this output.

![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/26864d29-56c1-473a-8539-aaa10b0f053c)

This is strange, as it doesn't print the flag fully. While the flag format is bcactf{...}, it's only printing bat{...}.

Let's take a look at the executable in Ghidra.

Opening the executable in Ghidra's CodeBrowser and pressing F5 nets us the generated pseudocode of this executable.

![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/d8a47854-cbd8-4408-9814-f11ff21ba579)

The second for loop uses the function ```putchar()``` to print letters out onto our screen. It is in that function that the above output is printed. However, there is something strange about this for loop. Specifically looking at the variable ```local_c```, it starts from 0, and increments itself twice every time the for loop is ran, once in line 23 and once in line 24. Most of the time, for loops increment themselves once, unless you are processing more than one byte of data at once, which in this scenario is not the case. Additionally, this variable incrementing twice would explain why it prints bat{...} instead of bcactf{...}: it's only printing every other character! With this understanding, we can now patch the file to remove one of the increments of ```local_c``` so that the executable will print the entire flag.

## Patching flagprinter

Double-clicking the for() function in the pseudocode brings us to a JBE command in the assembly code.

![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/a638b5e0-2695-49f2-aaf7-8890865df628)

JBE in assembly means Jump if Below or Equal. Essentially, the program will jump to the function ```LAB_0040067e```, which is the for loop.

Double-clicking ```LAB_0040067e``` brings us to the function, which comprises of this assembly code:

![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/4c185a51-ab3d-487d-8d78-c29d61b5890e)

The ```ADD      dword ptr [RBP + local_c], 0x1``` is actually the addition to ```local_c``` in line 23 in our pseudocode. Hence, if we right-click that line and click on Patch Instruction, and replace that statement with ```ADD      dword ptr [RBP + local_c], 0x0```, it will remove the addition of 1 to ```local_c``` in line 23, only leaving the increment of ```local_c``` in line 24. Press Enter to save the patched instruction and export it by clicking File -> Export Program. Take note that the format that we export it in should be Original File, rather than the Ghidra default Ghidra Zip File. 

Modifying the above statement actually changes our previous for loop to a while loop in the pseudocode, as seen here:

![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/e70ac4a9-bdfb-4889-afa6-2d644deb0d00)


## Obtaining the flag

Running the edited executable gives us this:

![image](https://github.com/kaien07/CTF-Writeups/assets/160471571/b21830ab-4232-43aa-87bf-a3d692d6a49f)

And there's our flag!

Flag: bcactf{c_c0dE_fIXeD_7H4NK5_762478276}
