s = '1F600'
print(chr(int(s, base=16)))
alphabet = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f)+1)])
print(alphabet)
print(len(alphabet))
