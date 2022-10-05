
file = open(
    "C:\\Users\\seanb\\Desktop\\python_learning\\basic\\write.txt", "w+", encoding="utf8")
file.write("Hello File, I am String")
file.seek(0)
print(file.read())
file.close()
