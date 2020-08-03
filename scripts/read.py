from sys import argv
path = argv[1]
file = open(path,"rb")
text = file.read().decode("utf-8")
file.close()
print(text)

