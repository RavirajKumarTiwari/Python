
f = open("data.txt", "w") #make a new file in output mode
f.write("Hello Ravi\n")  # Write strings of bytes to it
f.write("How are you?")  # Returns number of bytes written in Python 3.0
f.close()  # Close to flush output buffers to disk

print("----------------")
f = open("data.txt")  # 'r' is the default processing mode
text = f.read()  # Read entire file into a string
print(text)

print(text.split())

dir(f)
help(f.seek)

data = open('data.bin', 'rb').read()  # Open binary file
print(data)
# bytes string holds binary data
