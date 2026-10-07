with open("sample.txt", "w") as file:
    file.write("Hello world\n")
    file.write("Python is easy to learn\n")
    file.write("I like Python")
with open("sample.txt", "r") as file:
    text = file.read()
lines = text.splitlines()
words = text.split()
characters = len(text)
print("number of lines:", len(lines))
print("number of words:", len(words))
print("number of characters :",characters)
