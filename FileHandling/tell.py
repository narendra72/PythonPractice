f = open('myfile.txt','r')
text = f.read(4)
print("Current position:", f.tell()) 
print(text)
f.close()

# tell() tells the current position of the file pointer (in bytes)