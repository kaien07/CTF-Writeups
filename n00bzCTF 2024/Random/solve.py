out = "abcdefghij"
inp = [""] * 10
sampleinp = "edhiafcbgj"
sampleout = "aibgefhdcj"
mapdict = {}
for i in range(10):
    mapdict.update({i: sampleout.find(sampleinp[i])})
for elem in list(mapdict.keys()):
    inp[elem] = out[mapdict[elem]]
print("".join(inp))