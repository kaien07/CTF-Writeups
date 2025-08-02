changes = [-4, -3, -7, 5, -15, 2, 1, 3, 7, 3, -2, 4, -3, -4, -7, 9, -7, 5, -1, 2, -9, 6, -4, 0]
with open("string.txt", 'r') as f:
    data = f.readline()
flag = ""
for i in range(len(data)):
    flag += chr(ord(data[i]) - changes[i])
print(flag)
