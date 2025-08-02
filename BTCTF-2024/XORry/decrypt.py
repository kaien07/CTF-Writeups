with open("encrypted.txt", 'r') as f:
    data = f.read()
    for num in range(51):
        decrypt = ''.join([chr(ord(char) ^ num) for char in data])
        print(decrypt)
        print("\n")
