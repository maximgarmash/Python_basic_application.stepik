import simplecrypt
with open("encrypted.bin", "rb") as inp, open("passwords.txt", "r") as pwd, open("output.txt", "w") as out:
    encrypted, i = inp.read(), 1
    for line in pwd:
        try:
            out.write(simplecrypt.decrypt(line.rstrip(), encrypted).decode("utf-8"))
            break
        except BaseException:
            print(i, "Bad password")
            i += 1





