f = open("test1.txt", "w")
f.write("Hello\n")
f.write("world\n")


lines = ["line1", "line2", "line3"]
contents = "\n".join(lines)
f.write(contents)

f.close()