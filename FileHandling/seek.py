f = open("myfile.txt", "r")
f.seek(10)              
print(f.read())        
f.close()

# moves the file pointer to a specific position inside the file