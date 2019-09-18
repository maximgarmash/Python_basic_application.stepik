alphabet = ''
for character in range(int('1F600', base=16), int('1F64F', base=16) + 1):
    alphabet += chr(character)

shift = int(input())
string = str(input().strip())
cipher_str = ''
for character in string:
    if alphabet.index(character)+shift > len(alphabet) - 1:
        cipher_str += alphabet[alphabet.index(character)+shift-len(alphabet)*((alphabet.index(character)+shift)//80)]
    elif shift < 0:
        cipher_str += alphabet[alphabet.index(character)-abs(shift) % 80]
    else:
        cipher_str += alphabet[alphabet.index(character) + shift]

print("Result:", '"'+cipher_str+'"')