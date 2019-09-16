#4.3 Caesar cipher

alphabet = " abcdefghijklmnopqrstuvwxyz"
shift = int(input())
string = str(input().strip())
cipher_str = ''
for character in string:
    if alphabet.index(character)+shift > len(alphabet) - 1:
        cipher_str += alphabet[alphabet.index(character)+shift-len(alphabet)]
    # elif alphabet.index(character)+shift < 0:
    #     cipher_str += alphabet[alphabet.index(character)+shift-(len(alphabet)-1)]
    else:
        cipher_str += alphabet[alphabet.index(character)+shift]

print("Result:", '"'+cipher_str+'"')