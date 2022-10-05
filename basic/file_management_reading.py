
#(filename,acces(read, write or boths),buffering)
enc = 'utf-8'

file = open(
    "C:\\Users\\seanb\\Desktop\\python_learning\\basic\\file.txt", encoding="utf8")

print(file.read(4))

file.close()
