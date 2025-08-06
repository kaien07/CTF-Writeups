with open('Moss_in_the_Backrooms.jpg', 'rb') as f:
    a = f.read()

a = [i >> 7 for i in a]
p = []
for i in range(0, len(a), 8):
    s = [str(balls) for balls in a[i:i+8]]
    p.append(''.join(s))
# print(p)
print(''.join(p[:50]))
