with open("bf.txt", "r") as f:
    bf = f.read()
bflst = bf.split("<[-]>")
bflst2 = []
for elem in bflst:
    bflst2.append(elem.split("["))
for elem in bflst2:
    print(chr(elem[0].count("+") * elem[1].count("+")), end="")