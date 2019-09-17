#4.3 Caesar cipher

alphabet = " abcdefghijklmnopqrstuvwxyz"
shift = int(input())
string = str(input().strip())
cipher_str = ''
for character in string:
    if alphabet.index(character)+shift > len(alphabet) - 1:
        cipher_str += alphabet[alphabet.index(character)+shift-len(alphabet)*((alphabet.index(character)+shift)//27)]
    elif shift < 0:
        cipher_str += alphabet[alphabet.index(character)-abs(shift) % 27]
    else:
        cipher_str += alphabet[alphabet.index(character) + shift]

print("Result:", '"'+cipher_str+'"')