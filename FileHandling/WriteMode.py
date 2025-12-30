# Write mode
# we have myfile.txt
# and need to enter/write data inside this file..

f = open('myfile.txt','w')
f.write("Hello, this is my first file!\n")
f.write("Python is awesome language")
f.close()